from datetime import datetime


def write_log(
    event_type,
    location,
    key,
    old_value,
    new_value
):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(
        "registry_log.txt",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"[{timestamp}]\n"
        )

        file.write(
            f"{event_type}\n"
        )

        file.write(
            f"Location: {location}\n"
        )

        file.write(
            f"Key: {key}\n"
        )

        file.write(
            f"Old: {old_value}\n"
        )

        file.write(
            f"New: {new_value}\n"
        )

        file.write(
            "-" * 50 + "\n"
        )