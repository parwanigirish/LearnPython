import random

def play_rps():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)

    print(f"You chose {user_choice}, and the computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("You lose!")
        else:
            print("You win!")
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("You lose!")
        else:
            print("You win!")
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("You lose!")
        else:
            print("You win!")

play_rps()