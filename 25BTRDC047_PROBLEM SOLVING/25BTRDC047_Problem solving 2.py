print("STUDENT GRADING SYSTEM")

name = input("Enter student name: ")
total = 0

for i in range(1, 4):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total = total + marks

average = total / 3

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n--- RESULT ---")
print(f"Student Name: {name}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")