import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(a)


def natural_log(a):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    return math.log(a)


def factorial(a):
    if a < 0 or not float(a).is_integer():
        raise ValueError("Factorial only defined for non-negative integers")
    return math.factorial(int(a))


BINARY_OPS = {
    "1": ("Add", add),
    "2": ("Subtract", subtract),
    "3": ("Multiply", multiply),
    "4": ("Divide", divide),
    "5": ("Modulo", modulo),
    "6": ("Power", power),
    "7": ("Log base b of a", lambda a, b: math.log(a, b)),
}

UNARY_OPS = {
    "8": ("Square Root", square_root),
    "9": ("Natural Log", natural_log),
    "10": ("Factorial", factorial),
}


def read_number(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")


def show_menu():
    print()
    print("=" * 34)
    print("        Calculator")
    print("=" * 34)
    print("1-7: operations, 8-10: single-value functions, 0: exit")

    for key, (name, _) in BINARY_OPS.items():
        print(f"{key}. {name}")

    for key, (name, _) in UNARY_OPS.items():
        print(f"{key}. {name}")

    print("0. Exit")
    print("=" * 34)


def main():
    memory = 0.0
    last_result = None

    while True:
        show_menu()

        if last_result is not None:
            print(f"Last result: {last_result}")
        print(f"Memory: {memory}")

        choice = input("Enter option: ").strip().upper()

        if choice == "MS":
            if last_result is not None:
                memory = last_result
                print(f"Stored {memory} in memory")
            else:
                print("No result available to store")
            continue

        if choice == "M":
            print(f"Memory: {memory}")
            continue

        if choice == "0":
            print("Goodbye")
            break

        try:
            if choice in BINARY_OPS:
                _, function = BINARY_OPS[choice]
                a = read_number("First number: ")
                b = read_number("Second number: ")
                result = function(a, b)
            elif choice in UNARY_OPS:
                _, function = UNARY_OPS[choice]
                a = read_number("Number: ")
                result = function(a)
            else:
                print("Invalid option")
                continue
        except ValueError as error:
            print(error)
            continue

        print("Result:", result)
        last_result = result


if __name__ == "__main__":
    main()
