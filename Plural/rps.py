import imp


import random

choice = ["rock", "paper", "scissors"]
computer_coice = (random.choice(choice))

user_choice = input("Do you want rock-paper-scissors?: ")

if computer_coice == user_choice:
    print("Tie game ")
elif user_choice == "rock" and computer_coice == "scissors":
    print("You won!")
elif user_choice  == "paper" and computer_coice == "rock":
    print("You won")
elif user_choice  == "scissors" and computer_coice == "paper":
    print("You won")
else:
    print("Computer wins")