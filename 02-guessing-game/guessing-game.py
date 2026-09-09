# Number Guessing Game 

import random

computer_pick = random.randint(1, 100)

while True:

	user_input = int(input("Guess the number (Please enter an integer number between 1 and 100): "))

	if user_input == computer_pick:
		print("Hooray, You won. Congratulations")
		break

	elif user_input < computer_pick:
		print("Too Low. Try again")
		
	elif user_input > computer_pick:
		print("Too High. Try again")
		
	else:
		raise ValueError