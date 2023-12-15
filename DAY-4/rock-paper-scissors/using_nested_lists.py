# Let's try it out using nested Lists
import random
from data import data

users_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors."))
computer_choice = random.randint(0, 2)
results_matrix = [
    ["That's a draw 😉!", "You lose 👎!", "You Win 🏆!"],
    ["You Win 🏆!", "That's a draw 😉!", "You lose 👎!"],
    ["You lose 👎!", "You Win 🏆!", "That's a draw 😉!"],
]

if users_choice in (0, 1, 2):
    print('You chose: ')
    print(data[users_choice])
    print("Computer chose: ")
    print(data[computer_choice])
    print(results_matrix[users_choice][computer_choice])


