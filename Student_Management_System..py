class Student:
    def __init__(self, roll_no, name, age, course):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course

    def show_details(self):
        print("\nRoll No :", self.roll_no)
        print("Name    :", self.name)
        print("Age     :", self.age)
        print("Course  :", self.course)


students = []


def save_to_file():
    file = open("students.txt", "w")
    for student in students:
        file.write(f"{student.roll_no},{student.name},{student.age},{student.course}\n")
    file.close()


def load_from_file():
    try:
        file = open("students.txt", "r")
        for line in file:
            data = line.strip().split(",")
            student = Student(data[0], data[1], int(data[2]), data[3])
            students.append(student)
        file.close()
    except FileNotFoundError:
        pass


def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    student = Student(roll_no, name, age, course)
    students.append(student)
    save_to_file()

    print("Student Added Successfully!")


def view_students():
    if len(students) == 0:
        print("No Student Records Found!")
    else:
        print("\n----- Student Details -----")
        for student in students:
            student.show_details()
            print("---------------------------")


def search_student():
    roll_no = input("Enter Roll Number to Search: ")

    for student in students:
        if student.roll_no == roll_no:
            print("\nStudent Found!")
            student.show_details()
            return

    print("Student Not Found!")


def update_student():
    roll_no = input("Enter Roll Number to Update: ")

    for student in students:
        if student.roll_no == roll_no:
            student.name = input("Enter New Name: ")
            student.age = int(input("Enter New Age: "))
            student.course = input("Enter New Course: ")

            save_to_file()
            print("Student Updated Successfully!")
            return

    print("Student Not Found!")


def delete_student():
    roll_no = input("Enter Roll Number to Delete: ")

    for student in students:
        if student.roll_no == roll_no:
            students.remove(student)
            save_to_file()
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")


load_from_file()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")