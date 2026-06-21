import os


while True:

    print("\n====================================")
    print(" Windows Registry Monitoring System ")
    print("====================================")

    print("1. Create Baseline")
    print("2. Start Monitoring")
    print("3. Run Integrity Check")
    print("4. Malware Detection")
    print("5. Generate Report")
    print("6. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":

        os.system("python baseline.py")

    elif choice == "2":

        os.system("python monitor.py")

    elif choice == "3":

        os.system("python integrity_checker.py")

    elif choice == "4":

        os.system("python malware_detector.py")

    elif choice == "5":

        os.system("python report_generator.py")

    elif choice == "6":

        print("Exiting...")
        break

    else:

        print("Invalid choice")