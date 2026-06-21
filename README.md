Windows Registry Change Monitoring System

Overview

The Windows Registry Change Monitoring System is a Python-based cybersecurity project designed to monitor important Windows Registry locations and detect suspicious changes. Since the Windows Registry contains critical system and application settings, it is often targeted by malware to establish persistence, disable security features, or modify system behavior.

This project continuously monitors selected registry keys, detects additions, modifications, and deletions, compares the current registry state against a trusted baseline, and identifies registry configurations commonly associated with malware activity. The system also maintains logs of detected events and generates reports for analysis.

Project Objectives

The main objective of this project is to improve visibility into registry activity and help identify potentially malicious changes. The project focuses on:

* Monitoring critical startup-related registry locations.
* Detecting unauthorized registry modifications.
* Creating and maintaining a baseline registry snapshot.
* Verifying registry integrity through comparison with the baseline.
* Identifying common malware-related registry changes.
* Logging detected events with timestamps and details.
* Generating reports for security analysis.

Key Features

The system monitors commonly abused registry locations such as the Run and RunOnce keys under both HKEY_CURRENT_USER (HKCU) and HKEY_LOCAL_MACHINE (HKLM). These locations are frequently used by legitimate software for startup purposes, but they are also popular targets for malware persistence.

The monitoring component continuously checks these locations and identifies:

* Newly added registry entries
* Modified registry entries
* Deleted registry entries

A baseline snapshot can be created at any time and stored in JSON format. This snapshot serves as a trusted reference point that can later be compared with the current registry state to identify unexpected changes.

An integrity checking module compares the current registry configuration against the saved baseline and reports any differences, including missing, modified, or newly added entries.

The project also includes a malware detection module that checks registry locations commonly targeted by attackers. These checks include:

* Windows Defender configuration tampering
* User Account Control (UAC) modifications
* Shell replacement attempts through the Winlogon registry key

To support investigations and auditing, all detected events are recorded in a log file. Each log entry includes the event type, timestamp, registry location, affected key, previous value, and new value.

A reporting module generates a summary report containing event statistics and detailed information about detected changes.

Technologies Used

The project was developed using Python and relies primarily on the built-in `winreg` module for interacting with the Windows Registry. Additional modules such as `json`, `datetime`, `time`, and `os` were used for configuration management, logging, monitoring, and report generation.

PowerShell commands were used during testing to simulate registry modifications and verify the monitoring system.

Project Workflow

The project follows a simple workflow:

1. Load monitoring configuration.
2. Create or load a baseline registry snapshot.
3. Monitor registry keys at regular intervals.
4. Detect additions, modifications, and deletions.
5. Compare detected changes against known malware behavior patterns.
6. Generate alerts and logs.
7. Produce a final report for analysis.

Sample Detection Results

The system is capable of detecting:

* A new startup entry being added to the registry.
* An existing registry value being modified.
* A registry entry being removed.
* Security-related registry settings being altered.
* Suspicious shell replacements or disabled security controls.

Applications

This project can be useful in several cybersecurity scenarios, including:

* Malware analysis
* Incident response
* Registry forensics
* Security monitoring
* Blue Team operations
* System auditing

Future Improvements

Although the current implementation meets the project objectives, several enhancements can be added in the future. These include real-time notifications, scheduled execution through Task Scheduler, email alerts, graphical dashboards, PDF report generation, and integration with security monitoring platforms.

Conclusion

The Windows Registry Change Monitoring System demonstrates how registry monitoring can be used to detect suspicious activity and maintain system integrity. By combining continuous monitoring, baseline comparison, malware-pattern detection, logging, and reporting, the project provides a practical example of how defensive security tools can help identify and investigate unauthorized changes within a Windows environment.

Author:

Mohammed Noorul Hamdh

Cyber Security Intern

Unified Mentor
