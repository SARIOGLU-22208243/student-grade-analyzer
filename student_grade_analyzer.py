students = []

def show_menu():
    print("\n--- STUDENT GRADE ANALYZER ---")
    print("1. Add Student Grade")
    print("2. Show All Students")
    print("3. Calculate Average Grade")
    print("4. Show Highest and Lowest Grade")
    print("5. Show Passed and Failed Student Count")
    print("6. Exit")

def add_student():
    name = input("Student name: ").strip()
    grade_input = input("Grade: ").strip()

    if not grade_input.isdigit():
        print("Please enter a valid number.")
        return

    grade = int(grade_input)

    if grade < 0 or grade > 100:
        print("Grade must be between 0 and 100.")
        return

    students.append({"name": name, "grade": grade})
    print("Student added successfully.")

def show_students():
    if not students:
        print("No students added yet.")
        return

    print("\nStudent List:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student['name']} - {student['grade']}")

def calculate_average():
    if not students:
        print("No students added yet.")
        return

    total = sum(student["grade"] for student in students)
    average = total / len(students)
    print(f"Average grade: {average:.2f}")

def show_high_low():
    if not students:
        print("No students added yet.")
        return

    highest = max(students, key=lambda x: x["grade"])
    lowest = min(students, key=lambda x: x["grade"])

    print(f"Highest grade: {highest['name']} - {highest['grade']}")
    print(f"Lowest grade: {lowest['name']} - {lowest['grade']}")

def show_pass_fail():
    if not students:
        print("No students added yet.")
        return

    passed = sum(1 for student in students if student["grade"] >= 50)
    failed = sum(1 for student in students if student["grade"] < 50)

    print(f"Passed students: {passed}")
    print(f"Failed students: {failed}")

while True:
    show_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        calculate_average()
    elif choice == "4":
        show_high_low()
    elif choice == "5":
        show_pass_fail()
    elif choice == "6":
        print("Program is closing...")
        break
    else:
        print("Invalid choice. Please try again.")
