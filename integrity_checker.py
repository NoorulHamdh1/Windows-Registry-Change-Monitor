from baseline_loader import load_baseline
from monitor import get_registry_entries


def compare_with_baseline():

    baseline = load_baseline()

    if baseline is None:

        print("No baseline found.")
        return

    current = get_registry_entries()

    print("\n===== INTEGRITY CHECK REPORT =====\n")

    # ADDED
    for location in current:

        for key in current[location]:

            if key not in baseline.get(location, {}):

                print(f"[ADDED SINCE BASELINE] {key}")
                print(f"Location: {location}")
                print()

    # DELETED
    for location in baseline:

        for key in baseline[location]:

            if key not in current.get(location, {}):

                print(f"[MISSING FROM BASELINE] {key}")
                print(f"Location: {location}")
                print()

    # MODIFIED
    for location in baseline:

        for key in baseline[location]:

            if key in current.get(location, {}):

                if baseline[location][key] != current[location][key]:

                    print(f"[MODIFIED FROM BASELINE] {key}")
                    print(f"Location: {location}")
                    print(f"Baseline: {baseline[location][key]}")
                    print(f"Current : {current[location][key]}")
                    print()

    print("===== CHECK COMPLETE =====")


if __name__ == "__main__":
    compare_with_baseline()