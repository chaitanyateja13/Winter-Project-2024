from utils import add_student, view_students, search_student

def menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("\nExiting program. Goodbye!")
        break
    else:
        print("\nInvalid choice. Try again.\n")
