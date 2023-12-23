import random

import art

chances = 0

guess_num = random.randint(1, 100);
print(f"psssst... The guessed number is {guess_num}")


def play_game(diff):
    global chances, guess_num
    if diff == 'easy':
        chances = 10
        print(f'You have {chances} attempts remaining to guess the number.')
    else:
        chances = 5
        print(f'You have {chances} attempts remaining to guess the number.')
    while chances > 0:
        num = int(input("Make a guess: "))
        if num == guess_num:
            print(f"Wow, that's a correct guess. The number was {guess_num}")
            break
        elif num > guess_num:
            print("Too high.")
        elif num < guess_num:
            print("Too Low.")
        chances -= 1
        print(f'You have {chances} attempts remaining to guess the number.')
    if chances == 0:
        print("Oops ! Game over ❌")


game_is_on = True

while game_is_on:
    print(art.logo)
    print("Welcome to Sofia's Number Guessing Game 🎮 !")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("choose a difficulty 💪🫵. Type 'easy' or 'hard' or 'exit' : ").lower()
    if difficulty == 'easy' or difficulty == 'hard':
        play_game(difficulty)
    elif difficulty == 'exit':
        print("Goodbye. 👋")
        game_is_on = False
    else:
        print("Invalid Input, please try again.")
