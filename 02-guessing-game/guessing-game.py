# Number Guessing Game

import random

computer_pick = random.randint(1, 100)


def get_guess():
    while True:
        try:
            user_input = int(
                input("Guess the number (Enter an integer number between 1 and 100): ")
            )

            if user_input > 100 or user_input < 1:
                print("Please enter a number between 1 and 100")
                continue

            return user_input

        except ValueError:
            print("Invalid Input. Try again")


def check_guess(user_input, computer_pick):

        if user_input == computer_pick:
            return "Correct"

        elif user_input < computer_pick:
            return "Low"

        else:
            return "High"


def play_round():
    attempts = 0
    
    while True:
        guess = get_guess()
        attempts += 1
        result = check_guess(guess, computer_pick)

        if result == "Correct":
            print("Hooray, You won. Congratulations")
            break
        
        elif result == "Low":
            print("Too Low. Try again")
            
        elif result == "High":
            print("Too High. Try again")

    return attempts


def main():
    
    attempts = play_round()

    print(f"You got it in {attempts} attempts!")
    
main()
