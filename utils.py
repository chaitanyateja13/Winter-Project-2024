from student import Student
from data import students

def add_student():
    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))

    student = Student(roll_no, name, marks)
    students.append(student)

    print("\nStudent added successfully!\n")


def view_students():
    if not students:
        print("\nNo student records found.\n")
        return

    print("\nStudent Records:")
    print("-" * 30)
    for student in students:
        print(student)
    print("-" * 30)


def search_student():
    roll_no = int(input("Enter Roll Number to search: "))
    for student in students:
        if student.roll_no == roll_no:
            print("\nStudent Found:")
            print(student)
            return
    print("\nStudent not found.\n")
