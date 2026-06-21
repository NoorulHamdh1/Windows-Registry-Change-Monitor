import json


def load_baseline():

    try:

        with open("baseline.json", "r") as file:

            baseline = json.load(file)

        return baseline

    except FileNotFoundError:

        return None