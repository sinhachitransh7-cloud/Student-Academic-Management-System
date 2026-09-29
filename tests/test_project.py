def test_average():
    marks = [80, 70, 90]

    average = sum(marks) / len(marks)

    assert average == 80


def test_assignment_status():
    assignment = {
        "title": "Python Project",
        "status": "Pending"
    }

    assignment["status"] = "Completed"

    assert assignment["status"] == "Completed"


print("All tests passed!")
