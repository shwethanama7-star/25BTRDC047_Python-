
# try:
#     file = open("application.log", "r")

#     error_count = 0
#     warning_count = 0
#     info_count = 0

#     for line in file:
#         if "ERROR" in line:
#             error_count += 1
#         elif "WARNING" in line:
#             warning_count += 1
#         elif "INFO" in line:
#             info_count += 1

#     file.close()

#     print("--- LOG FILE SUMMARY ---")
#     print("ERROR:", error_count)
#     print("WARNING:", warning_count)
#     print("INFO:", info_count)

# except FileNotFoundError:
#     print("Log file not found!")

# except Exception as e:
#     print("An error occurred:", e)




# while True:
#     print("\n--- STUDENT DATA MANAGER ---")
#     print("1. Add Student")
#     print("2. Display Students")
#     print("3. Search Student")
#     print("4. Update Student")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         roll = input("Enter roll number: ")
#         name = input("Enter student name: ")
#         marks = input("Enter marks: ")

#         with open("students.txt", "a") as file:
#             file.write(roll + "," + name + "," + marks + "\n")

#         print("Student record added successfully!")

#     elif choice == "2":
#         try:
#             with open("students.txt", "r") as file:
#                 print("\n--- STUDENT RECORDS ---")
#                 for line in file:
#                     print(line.strip())
#         except FileNotFoundError:
#             print("No student records found!")

#     elif choice == "3":
#         roll = input("Enter roll number to search: ")
#         found = False

#         try:
#             with open("students.txt", "r") as file:
#                 for line in file:
#                     data = line.strip().split(",")

#                     if data[0] == roll:
#                         print("Roll Number:", data[0])
#                         print("Name:", data[1])
#                         print("Marks:", data[2])
#                         found = True
#                         break

#             if not found:
#                 print("Student not found!")

#         except FileNotFoundError:
#             print("Student file not found!")

#     elif choice == "4":
#         roll = input("Enter roll number to update: ")
#         found = False
#         records = []

#         try:
#             with open("students.txt", "r") as file:
#                 records = file.readlines()

#             with open("students.txt", "w") as file:
#                 for line in records:
#                     data = line.strip().split(",")

#                     if data[0] == roll:
#                         name = input("Enter new name: ")
#                         marks = input("Enter new marks: ")
#                         line = roll + "," + name + "," + marks + "\n"
#                         found = True

#                     file.write(line)

#             if found:
#                 print("Student record updated!")
#             else:
#                 print("Student not found!")

#         except FileNotFoundError:
#             print("Student file not found!")

#     elif choice == "5":
#         print("Exiting Student Data Manager.")
#         break

#     else:
#         print("Invalid choice!")



import csv

try:
    with open("employees.csv", "r") as file:

        reader = csv.DictReader(file)

        total_salary = 0

        print("\n--- PAYROLL SUMMARY ---")

        for employee in reader:

            name = employee["Name"]
            basic = float(employee["Basic"])
            hra = float(employee["HRA"])
            da = float(employee["DA"])

            gross = basic + hra + da

            pf = basic * 0.12
            tax = gross * 0.05

            deduction = pf + tax
            net_salary = gross - deduction

            total_salary += net_salary

            print("\nEmployee:", name)
            print("Gross Salary:", gross)
            print("PF Deduction:", pf)
            print("Tax Deduction:", tax)
            print("Total Deduction:", deduction)
            print("Net Salary:", net_salary)

        print("\nTotal Salary Paid:", total_salary)

except FileNotFoundError:
    print("Employee CSV file not found!")

except ValueError:
    print("Invalid salary data!")



