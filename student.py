from validators import get_non_empty

student = {}


def add_student():
    name = get_non_empty("Enter student name: ")
    roll_no = get_non_empty("Enter roll number: ")
    branch = get_non_empty("Enter branch: ")

    student["name"] = name
    student["roll_no"] = roll_no
    student["branch"] = branch

    print("\n✅ Student profile created successfully!")


def view_student():
    if not student:
        print("\n❌ No student profile found.")
        return

    print("\n" + "-" * 40)
    print("           STUDENT PROFILE")
    print("-" * 40)

    print(f"Name     : {student['name']}")
    print(f"Roll No  : {student['roll_no']}")
    print(f"Branch   : {student['branch']}")

    print("-" * 40)


def update_student():
    if not student:
        print("\n❌ No student profile found.")
        return

    print("\nUpdate Student Profile")

    name = get_non_empty("Enter new name: ")
    roll_no = get_non_empty("Enter new roll number: ")
    branch = get_non_empty("Enter branch: ")

    student["name"] = name
    student["roll_no"] = roll_no
    student["branch"] = branch

    print("\n✅ Student profile updated successfully!")