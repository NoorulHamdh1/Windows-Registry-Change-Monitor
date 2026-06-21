import winreg
import json

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


baseline = get_registry_entries()

with open("baseline.json", "w") as file:

    json.dump(
        baseline,
        file,
        indent=4
    )

print("Baseline created successfully.")