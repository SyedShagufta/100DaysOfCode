import data
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors."))
computer_choice = random.randint(0, 2)

if user_choice in (0, 1, 2):
    print("You Chose:")
    print(data.data[user_choice])

    print("Computer Chose:")
    print(data.data[computer_choice])

    if user_choice == 0 and computer_choice == 2 or user_choice == 2 and computer_choice == 1 or user_choice == 1 and computer_choice == 0:
        print("You Win 🏆!")
    elif user_choice == computer_choice:
        print("Oops that's a draw!")
    else:
        print("You lose 👎!")

else:
    print("Invalid Input.")
    