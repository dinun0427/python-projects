# Number Guessing Game

import random

computer_pick = random.randint(1, 100)
attempts = 0

def get_guess():
    while True:
		try:
			user_input = int(input("Guess the number (Please enter an integer number between 1 and 100): "))
         
        	if user_input > 100 or user_input < 1:
            	print("Please enter a number between 1 and 100")
            	continue
         
			return user_input
        
		except ValueError:
        	print("Invalid Input. Try again")

while True:
		user_input = get_guess()
        attempts += 1
        

        if user_input == computer_pick:
            print("Hooray, You won. Congratulations")
            break

        elif user_input < computer_pick:
            print("Too Low. Try again")

        elif user_input > computer_pick:
            print("Too High. Try again")


print(f"You got it in {attempts} attempts!")