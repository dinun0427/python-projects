# CLI calculator


def add(a, b):
    result = a + b
    return result


def substract(a, b):
    result = a - b
    return result


def multiply(a, b):
    result = a * b
    return result


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


def calculate(a, b, operator):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return substract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)
    else:
        raise ValueError(f"Invalid operator: {operator}")


def main():
    print("Welcome to the CLI Calculator!")
    print("Use these arithmetic operators only (+, -, *, /)\n")

    while True:
        user_input = input("Enter two numbers and the operator (e.g. 2 + 2): ")
        if user_input == "exit" or user_input == "quit":
            print("Exiting the calculator. Goodbye!")
            break
        else:
            try:
                num1_str, operator, num2_str = user_input.split()

                num1 = float(num1_str)
                num2 = float(num2_str)
            except ValueError:
                print("Error: Please enter valid numbers.")
                continue

            try:
                result = calculate(num1, num2, operator)
                print(f"Your calculation : {result}")
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
            except ValueError as e:
                print(f"Error: {e}")


main()
