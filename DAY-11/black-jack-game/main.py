# ------------------------- Our Black jack rules ---------------------------------- #
import os
import random

import art

# The deck is unlimited in size.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(list_of_cards):
    if {11, 10}.issubset(list_of_cards):
        return 0
    elif {11}.issubset(list_of_cards) and sum(list_of_cards) >= 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
        return sum(list_of_cards)
    else:
        return sum(list_of_cards)


def compare(u_score, c_score):
    if u_score == c_score:
        print("Oops.. It's a Draw. 🎭")
    elif c_score == 0:
        print("Computer has BlackJack.. You lose. ☹️")
    elif u_score == 0:
        print('You got a BlackJack. You Win. 😉🥇')
    elif u_score > 21:
        print("You have gone over 21. You lose. 😞")
    elif c_score > 21:
        print("Computer got over 21. You Win. 😉🫵💪")
    else:
        if u_score > c_score:
            print("You win. 🥇")
        else:
            print("Computer wins. 🤖")


def play_game():
    global user_score, computer_score
    print(art.logo)
    user_cards = []
    computer_cards = []
    for _ in range(1, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_ended = False

    while not game_ended:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"  You cards: {user_cards}, current score: {user_score}")
        print(f"  Computer cards: {computer_cards}, computer score: {computer_score}")
        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            game_ended = True
        else:
            choice = input("Do you want to take another card? Type 'y' or 'n': ")
            if choice == 'y':
                user_cards.append(deal_card())
            else:
                print("Game Ended.")
                game_ended = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    compare(user_score, computer_score)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    play_game()
