# CLI calculator

print("Welcome to the CLI Calculator!")
print("Use these arethmatic operators only (+, -, *, /)\n")

user_input = input("Enter two numbers and the operator (e.g. 2 + 2): ")

num1_str, operator, num2_str = user_input.split()

num1 = float(num1_str)
num2 = float(num2_str)

if operator == "+":
	result = num1 + num2
elif operator == "-":
	result = num1 - num2
elif operator == "*":
	result = num1 * num2
elif operator == "/":
	result = num1 / num2
else:
	print("Invalid operator")

print(f"Your calculation : {result}")






