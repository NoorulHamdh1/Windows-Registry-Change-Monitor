from logger import write_log
import winreg
import time

MONITORED_KEYS = [
    (
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        "HKCU_Run"
    ),
    (
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\RunOnce",
        "HKCU_RunOnce"
    ),
    (
        winreg.HKEY_LOCAL_MACHINE,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        "HKLM_Run"
    ),
    (
        winreg.HKEY_LOCAL_MACHINE,
        r"Software\Microsoft\Windows\CurrentVersion\RunOnce",
        "HKLM_RunOnce"
    )
]


def get_registry_entries():

    all_entries = {}

    for hive, path, label in MONITORED_KEYS:

        all_entries[label] = {}

        try:

            key = winreg.OpenKey(hive, path)

            i = 0

            while True:

                try:

                    name, value, _ = winreg.EnumValue(key, i)

                    all_entries[label][name] = value

                    i += 1

                except OSError:
                    break

            winreg.CloseKey(key)

        except FileNotFoundError:
            pass

        except Exception as e:
            print(f"Error reading {label}: {e}")

    return all_entries


def start_monitor():

    previous_state = get_registry_entries()

    print("\n===== INITIAL REGISTRY SNAPSHOT =====\n")

    for location in previous_state:

        print(
            f"{location}: "
            f"{len(previous_state[location])} entries"
        )

    print("\n=====================================\n")

    print("Monitoring started...")
    print("Checking every 10 seconds...\n")

    while True:

        time.sleep(10)

        current_state = get_registry_entries()

        # ADDED
        for location in current_state:

            for key in current_state[location]:

                if key not in previous_state.get(location, {}):

                    new_value = (
                        current_state[location][key]
                        if current_state[location][key]
                        else "NIL"
                    )

                    print(f"\n[ADDED] {key}")
                    print(f"Location: {location}")
                    print("Old: NIL")
                    print(f"New: {new_value}")

                    write_log(
                        "[ADDED]",
                        location,
                        key,
                        "NIL",
                        new_value
                    )

        # DELETED
        for location in previous_state:

            for key in previous_state[location]:

                if key not in current_state.get(location, {}):

                    old_value = (
                        previous_state[location][key]
                        if previous_state[location][key]
                        else "NIL"
                    )

                    print(f"\n[DELETED] {key}")
                    print(f"Location: {location}")
                    print(f"Old: {old_value}")
                    print("New: NIL")

                    write_log(
                        "[DELETED]",
                        location,
                        key,
                        old_value,
                        "NIL"
                    )

        # MODIFIED
        for location in previous_state:

            for key in previous_state[location]:

                if key in current_state.get(location, {}):

                    if (
                        previous_state[location][key]
                        != current_state[location][key]
                    ):

                        old_value = (
                            previous_state[location][key]
                            if previous_state[location][key]
                            else "NIL"
                        )

                        new_value = (
                            current_state[location][key]
                            if current_state[location][key]
                            else "NIL"
                        )

                        print(f"\n[MODIFIED] {key}")
                        print(f"Location: {location}")
                        print(f"Old: {old_value}")
                        print(f"New: {new_value}")

                        write_log(
                            "[MODIFIED]",
                            location,
                            key,
                            old_value,
                            new_value
                        )

        previous_state = current_state.copy()


if __name__ == "__main__":
    start_monitor()