from student import add_student, view_student, update_student, student
from assignments import add_assignment, view_assignments, mark_completed, delete_assignment, assignments
from marks import add_marks, view_marks, calculate_average, highest_lowest, marks
from reports import show_report
from storage import save_data, load_data


def show_dashboard():
    print("\n" + "=" * 45)
    print("              🎓 CAMPUS TRACK")
    print("       Student Academic Management")
    print("=" * 45)

    print("\n1. 👤 Student Profile")
    print("2. 📝 Assignment Manager")
    print("3. 📊 Marks & Performance")
    print("4. 📋 Academic Report")
    print("5. 🚪 Exit")

    print("\n" + "-" * 45)


def student_menu():
    while True:
        print("\n" + "-" * 35)
        print("       STUDENT PROFILE")
        print("-" * 35)

        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            break
        else:
            print("\n❌ Invalid choice.")


def assignment_menu():
    while True:
        print("\n" + "-" * 35)
        print("       ASSIGNMENT MANAGER")
        print("-" * 35)

        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Mark Completed")
        print("4. Delete Assignment")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_assignment()
        elif choice == "2":
            view_assignments()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_assignment()
        elif choice == "5":
            break
        else:
            print("\n❌ Invalid choice.")


def marks_menu():
    while True:
        print("\n" + "-" * 35)
        print("       MARKS & PERFORMANCE")
        print("-" * 35)

        print("1. Add Marks")
        print("2. View Marks")
        print("3. Calculate Average")
        print("4. Highest & Lowest")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_marks()
        elif choice == "2":
            view_marks()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            highest_lowest()
        elif choice == "5":
            break
        else:
            print("\n❌ Invalid choice.")


def main():
    data = load_data()

    student.update(data["student"])
    assignments.extend(data["assignments"])
    marks.update(data["marks"])

    while True:
        show_dashboard()

        choice = input("Enter your choice: ")

        if choice == "1":
            student_menu()
        elif choice == "2":
            assignment_menu()
        elif choice == "3":
            marks_menu()
        elif choice == "4":
            show_report()
        elif choice == "5":
            save_data(student, assignments, marks)
            print("\nData saved successfully!")
            print("Thank you for using CampusTrack!")
            break
        else:
            print("\n❌ Invalid choice. Please enter 1 to 5.")


if __name__ == "__main__":
    main()