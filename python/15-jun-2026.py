def greet(name):
    print("Hello,", name)


def add_numbers(*args):
    print("Numbers:", args)
    print("Sum:", sum(args))


def student_info(**kwargs):
    print("Student Details:")
    for key, value in kwargs.items():
        print(key, ":", value)


# Function calls (IMPORTANT)
greet("Kailash")

add_numbers(10, 20, 30)

student_info(name="Alice", age=30, city="New York")