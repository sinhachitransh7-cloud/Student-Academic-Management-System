marks = {}


def add_marks():
    subject = input("Enter subject name: ")
    mark = float(input("Enter marks: "))

    marks[subject] = mark

    print("\n✅ Marks added successfully!")


def view_marks():
    if not marks:
        print("\n❌ No marks found.")
        return

    print("\n" + "=" * 40)
    print("          MARKS & PERFORMANCE")
    print("=" * 40)

    for subject, mark in marks.items():
        print(f"{subject:<20} {mark}")

    print("=" * 40)


def calculate_average():
    if not marks:
        print("\n❌ No marks found.")
        return

    average = sum(marks.values()) / len(marks)

    print(f"\n📊 Average Marks: {average:.2f}")


def highest_lowest():
    if not marks:
        print("\n❌ No marks found.")
        return

    highest_subject = max(marks, key=marks.get)
    lowest_subject = min(marks, key=marks.get)

    print(f"\n🏆 Highest: {highest_subject} - {marks[highest_subject]}")
    print(f"📉 Lowest: {lowest_subject} - {marks[lowest_subject]}")