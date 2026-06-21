from datetime import datetime


def generate_report():

    try:

        with open(
            "registry_log.txt",
            "r",
            encoding="utf-8"
        ) as log_file:

            log_data = log_file.read()

    except FileNotFoundError:

        print("No registry_log.txt found.")
        return

    added_count = log_data.count("[ADDED]")
    modified_count = log_data.count("[MODIFIED]")
    deleted_count = log_data.count("[DELETED]")

    total_events = (
        added_count +
        modified_count +
        deleted_count
    )

    report = f"""
WINDOWS REGISTRY CHANGE REPORT

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

==================================================

SUMMARY

Total Events   : {total_events}
Added Events   : {added_count}
Modified Events: {modified_count}
Deleted Events : {deleted_count}

==================================================

EVENT DETAILS

{log_data}

==================================================
END OF REPORT
==================================================
"""

    with open(
        "final_report.txt",
        "w",
        encoding="utf-8"
    ) as report_file:

        report_file.write(report)

    print("Report generated successfully.")
    print("Saved as final_report.txt")


if __name__ == "__main__":
    generate_report()