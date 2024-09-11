#Christian Brown

from random import choice

while True:
    CHOICES = ["rock", "paper", "scissors"]


    computer_choice = choice(CHOICES)

    user_choice = input("Do you want - rock, paper, or scissors?\n").lower()
    if user_choice == "q":
        print("\nGoodbye, Thanks for playing!\n")
        break
    
    if computer_choice == user_choice:  
        print(f"\nTIE! Computer chose {computer_choice}.\n")
    elif user_choice == "rock" and computer_choice == "scissors" or user_choice == "scissors" and computer_choice == "paper" or user_choice == "paper" and computer_choice == "rock":
       print(f"\nWIN! Computer chose {computer_choice}.\n")
    else:
        print(f"\nLOSE! Computer chose {computer_choice}.\n")
    
    if user_choice not in CHOICES:
        print("\nInvalid choice. Try again.\n")
    
