import random

options = ["rock","paper","scissors"]

def gameStart():
    ai_choice = random.choice(options)

    result = input("What do you choose?:" ).lower()

    if result not in options:
        print("Please select rock, paper, or scissors")
        return
    
    if result == ai_choice:
        print("Tie")
    elif result == "paper" and ai_choice == "scissors":
        print("You lose!")
    elif result == "rock" and ai_choice == "paper":
        print("You Lose!")
    elif result == "scissors" and ai_choice == "rock":
        print("You Lose!")
    else:
        print("You win!")
    
    print("The ai chose: " + ai_choice)



gameStart()