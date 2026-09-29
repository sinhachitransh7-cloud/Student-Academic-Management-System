import json


def save_data(student, assignments, marks):
    data = {
        "student": student,
        "assignments": assignments,
        "marks": marks
    }

    with open("campus_data.json", "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    try:
        with open("campus_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "student": {},
            "assignments": [],
            "marks": {}
        }