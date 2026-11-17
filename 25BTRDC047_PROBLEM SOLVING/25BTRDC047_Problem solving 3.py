
# students = {}

# def add_student():
#     name = input("Enter student name: ")
#     if name not in students:
#         students[name] = {"Present": 0, "Absent": 0}
#         print("Student added successfully!")
#     else:
#         print("Student already exists!")

# def mark_attendance():
#     name = input("Enter student name: ")

#     if name in students:
#         status = input("Enter P for Present or A for Absent: ").upper()

#         if status == "P":
#             students[name]["Present"] += 1
#             print("Attendance marked Present!")
#         elif status == "A":
#             students[name]["Absent"] += 1
#             print("Attendance marked Absent!")
#         else:
#             print("Invalid status!")
#     else:
#         print("Student not found!")

# def display_attendance():
#     print("\nAttendance Details")
#     for name, record in students.items():
#         total = record["Present"] + record["Absent"]

#         if total > 0:
#             percentage = (record["Present"] / total) * 100
#         else:
#             percentage = 0

#         print(name, "Present:", record["Present"],
#               "Absent:", record["Absent"],
#               "Percentage:", round(percentage, 2), "%")

# def check_shortage():
#     threshold = float(input("Enter attendance threshold: "))

#     for name, record in students.items():
#         total = record["Present"] + record["Absent"]

#         if total > 0:
#             percentage = (record["Present"] / total) * 100
#         else:
#             percentage = 0

#         if percentage < threshold:
#             print(name, "has low attendance:", round(percentage, 2), "%")


# while True:
#     print("\n1. Add Student")
#     print("2. Mark Attendance")
#     print("3. Display Attendance")
#     print("4. Check Low Attendance")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         add_student()
#     elif choice == "2":
#         mark_attendance()
#     elif choice == "3":
#         display_attendance()
#     elif choice == "4":
#         check_shortage()
#     elif choice == "5":
#         print("Exiting Attendance Tracker!")
#         break
#     else:
#         print("Invalid choice!")



products = {}

def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity sold: "))
    price = float(input("Enter price per product: "))

    if quantity < 0 or price < 0:
        print("Invalid quantity or price!")
        return

    if name in products:
        products[name]["Quantity"] += quantity
        products[name]["Price"] = price
    else:
        products[name] = {
            "Quantity": quantity,
            "Price": price
        }

    print("Product record added successfully!")

def display_sales():
    print("\nSales Report")
    total_sales = 0

    for name, details in products.items():
        revenue = details["Quantity"] * details["Price"]
        total_sales += revenue

        print(name, "Quantity:", details["Quantity"],
              "Revenue:", revenue)

    print("Total Sales:", total_sales)

def highest_selling():
    if not products:
        print("No products available!")
        return

    highest = max(products, key=lambda x: products[x]["Quantity"])

    print("Highest Selling Product:", highest)
    print("Quantity Sold:", products[highest]["Quantity"])

while True:
    print("\n1. Add Product")
    print("2. Display Sales")
    print("3. Highest Selling Product")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        display_sales()
    elif choice == "3":
        highest_selling()
    elif choice == "4":
        print("Exiting Sales Analyzer!")
        break
    else:
        print("Invalid choice!")

