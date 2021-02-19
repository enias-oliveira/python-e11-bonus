import csv
from re import search


def find_blood_donors_1(filename):
    def is_donor_1(donor):

        name = "Victoria"
        blood_group = "AB-"
        age = "60"
        mail = "gmail"

        regex = f"\w+@{mail}.com"

        return (
            (name in donor["name"])
            and (blood_group == donor["blood_group"])
            and (age == donor["age"])
            and (search(regex, donor["mail"]))
        )

    def get_donors_1():
        with open(filename, "r") as readable_file:

            reader = csv.DictReader(readable_file)

            for donor in reader:
                if is_donor_1(donor):
                    yield {"name": donor["name"], "mail": donor["mail"]}

    return [donor for donor in get_donors_1()]


def find_blood_donors_2(filename):
    def is_donor_2(donor):
        last_name = "Norris"
        genre = "M"
        blood_group = "B+"
        min_age = 30
        max_age = 50
        mail = "yahoo"

        regex = f"\w+@{mail}.com"

        donor_last_name = donor["name"].split()[1]

        return (
            (last_name == donor_last_name)
            and (genre == donor["sex"])
            and (blood_group == donor["blood_group"])
            and (min_age <= int(donor["age"]) and max_age >= int(donor["age"]))
            and (search(regex, donor["mail"]))
        )

    def get_donors_2():
        with open(filename, "r") as readable_file:

            reader = csv.DictReader(readable_file)

            for donor in reader:
                if is_donor_2(donor):
                    yield {"name": donor["name"], "mail": donor["mail"]}

    return [donor for donor in get_donors_2()]
