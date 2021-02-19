import csv
from re import search


def is_donor(donor, name, blood_group, age, mail):

    regex = f"\w+@{mail}.com"

    return (
        (name in donor["name"])
        and (blood_group == donor["blood_group"])
        and (age == donor["age"])
        and (search(regex, donor["mail"]))
    )


def find_blood_donors_1(filename):

    name = "Victoria"
    blood_group = "AB-"
    age = "60"
    mail = "gmail"

    with open(filename, "r") as readable_file:

        reader = csv.DictReader(readable_file)

        for donor in reader:
            if is_donor(donor, name, blood_group, age, mail):

                result = {"name": donor["name"], "mail": donor["mail"]}

                yield result


def find_blood_donors_2(filename):
    ...
