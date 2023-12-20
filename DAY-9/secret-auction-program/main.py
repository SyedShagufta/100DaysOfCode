# we can use clear() to clear the output of the screen
import os
from art import logo

# Create a dictionary to store the user and their bids
auction_dict = {}

print(logo)

print("Welcome to Sofia's Secret Auction Program. 🎉✨🥳")
game_is_on = True


def winner():
    max_value = max(auction_dict.values())
    max_keys = [key for key, value in auction_dict.items() if value == max_value]

    if len(max_keys) == 1:
        print(f"The Winner is {max_keys[0]} with highest bid {max_value}. 🥇🎉")
    else:
        print("Unfortunately, It's a tie. 🏆")
        for bidder in max_keys:
            print(f"The Winner is {bidder} with the bid {max_value}. 🎉")


while game_is_on:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction_dict[name] = bid
    more_players = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if more_players == 'yes' or more_players == 'y':
        os.system('cls')
    else:
        game_is_on = False
        os.system('cls')
        winner()
