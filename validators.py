def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Please enter a value.")


def get_mark(prompt):
    while True:
        try:
            mark = float(input(prompt))

            if 0 <= mark <= 100:
                return mark

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a number.")