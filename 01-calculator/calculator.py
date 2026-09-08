# CLI calculator

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
        if operator == "+":
            result = num1 + num2
            print(f"Your calculation : {result}")
        elif operator == "-":
            result = num1 - num2
            print(f"Your calculation : {result}")
        elif operator == "*":
            result = num1 * num2
            print(f"Your calculation : {result}")
        elif operator == "/":
            try:
                result = num1 / num2
                print(f"Your calculation : {result}")
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
                continue
        else:
            print("Invalid operator")
