assignments = []


def add_assignment():
    title = input("Enter assignment title: ")
    subject = input("Enter subject: ")
    deadline = input("Enter deadline: ")

    assignment = {
        "title": title,
        "subject": subject,
        "deadline": deadline,
        "status": "Pending"
    }

    assignments.append(assignment)

    print("\n✅ Assignment added successfully!")


def view_assignments():
    if not assignments:
        print("\n❌ No assignments found.")
        return

    print("\n" + "=" * 50)
    print("              ASSIGNMENTS")
    print("=" * 50)

    for i, assignment in enumerate(assignments, 1):
        print(f"\n{i}. {assignment['title']}")
        print(f"   Subject  : {assignment['subject']}")
        print(f"   Deadline : {assignment['deadline']}")
        print(f"   Status   : {assignment['status']}")

    print("\n" + "=" * 50)


def mark_completed():
    if not assignments:
        print("\n❌ No assignments found.")
        return

    view_assignments()

    choice = int(input("\nEnter assignment number to mark completed: "))

    if 1 <= choice <= len(assignments):
        assignments[choice - 1]["status"] = "Completed"
        print("\n✅ Assignment marked as completed!")
    else:
        print("\n❌ Invalid assignment number.")


def delete_assignment():
    if not assignments:
        print("\n❌ No assignments found.")
        return

    view_assignments()

    choice = int(input("\nEnter assignment number to delete: "))

    if 1 <= choice <= len(assignments):
        assignments.pop(choice - 1)
        print("\n✅ Assignment deleted successfully!")
    else:
        print("\n❌ Invalid assignment number.")