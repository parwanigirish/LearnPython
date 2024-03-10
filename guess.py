import random

def guess_game():
    number = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")

    print(f"Congratulations! You guessed the number in {attempts} attempts.")

guess_game()