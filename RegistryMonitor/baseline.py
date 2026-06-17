import winreg
import json

KEY_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"

def get_run_entries():
    data = {}

    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            KEY_PATH
        )

        i = 0

        while True:
            try:
                name, value, _ = winreg.EnumValue(key, i)

                data[name] = value

                i += 1

            except OSError:
                break

        winreg.CloseKey(key)

    except Exception as e:
        print("Error:", e)

    return data


entries = get_run_entries()

with open("baseline.json", "w") as file:
    json.dump(entries, file, indent=4)

print("Baseline created successfully")