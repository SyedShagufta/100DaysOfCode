import random

from data import data

game_over = False
user_score = 0
computer_score = 0
counter = 0
print("Welcome to Rock 🪨 Paper 🗞️ Scissors ✂ Game ")
while not game_over:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors."))
    computer_choice = random.randint(0, 2)
    counter += 1
    if user_choice in (0, 1, 2):
        print("You Chose:")
        print(data[user_choice])

        print("Computer Chose:")
        print(data[computer_choice])

        if user_choice == 0 and computer_choice == 2 or user_choice == 2 and computer_choice == 1 or user_choice == 1 and computer_choice == 0:
            print("You Win 🏆!")
            user_score += 1
        elif user_choice == computer_choice:
            print("Oops that's a draw!")
        else:
            print("You lose 👎!")
            computer_score += 1
        print(f"User Score: {user_score}/{counter}.")
        print(f"Computer Score: {computer_score}/{counter}.")
        still_wanna_play = input("Do you want to continue playing? Yes or No.").lower()
        if still_wanna_play == 'no' or still_wanna_play == 'n':
            print("--------------------------------------------------------")
            print(f"Final User Score: {user_score}/{counter}.")
            print(f"Final Computer Score: {computer_score}/{counter}.")
            game_over = True
    else:
        print("Invalid Input. Try Again ! 🎃")
