students = {}

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        marks = int(input("Enter marks: "))

        students[roll_number] = {
            "name": name,
            "marks": marks
        }

        print("✅ Student added successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("📚 No students found.")
        else:
            for roll_number, details in students.items():
                print("\nRoll No:", roll_number)
                print("Name:", details["name"])
                print("Marks:", details["marks"])

    elif choice == 3:
        roll_number = input("Enter roll number: ")

        if roll_number in students:
            print("Name:", students[roll_number]["name"])
            print("Marks:", students[roll_number]["marks"])
        else:
            print("❌ Student not found!")

    elif choice == 4:
        roll_number = input("Enter roll number: ")

        if roll_number in students:
            marks = int(input("Enter new marks: "))
            students[roll_number]["marks"] = marks
            print("✅ Marks updated successfully!")
        else:
            print("❌ Student not found!")

    elif choice == 5:
        roll_number = input("Enter roll number: ")

        if roll_number in students:
            del students[roll_number]
            print("🗑️ Student deleted successfully!")
        else:
            print("❌ Student not found!")

    elif choice == 6:
        print("👋 Thank you for using Student Management System!")
        break

    else:
        print("❌ Invalid choice!")