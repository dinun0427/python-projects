# Number Guessing Game

import random


def get_guess(low, high):
    while True:
        try:
            user_input = int(
                input(
                    f"Guess the number (Enter an integer number between {low} and {high}): "
                )
            )

            if user_input > high or user_input < low:
                print(f"Please enter a number between {low} and {high}")
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


def play_round(computer_pick, low, high):
    attempts = 0

    while True:
        guess = get_guess(low, high)
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
    
    while True:
        while True:
            try:
                level = int(
                    input(
                        "Pick a Level of Difficulty\nEnter 1 for Easy (1-50)\nEnter 2 for Medium (1-100)\nEnter 3 for Hard (1-500)\n: "
                    )
                )

                if level == 1:
                    low, high = 1, 50
                    computer_pick = random.randint(low, high)
                    break
                elif level == 2:
                    low, high = 1, 100
                    computer_pick = random.randint(low, high)
                    break
                elif level == 3:
                    low, high = 1, 500
                    computer_pick = random.randint(low, high)
                    break
                else:
                    print("Invalid Input. Try again")
                    continue

            except ValueError:
                print("Invalid Input. Try again")
                continue

        attempts = play_round(computer_pick, low, high)

        print(f"You got it in {attempts} attempts!")


        play_again = input(
            "If you want to play again, type 'yes'. If you want to exit, type 'no': "
        )
        if play_again.lower() != "yes":
            break


main()
