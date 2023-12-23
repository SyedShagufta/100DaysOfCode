import os

import art
import random
from game_data import data

game_is_on = True
score = 0

print(art.logo)
A = random.choice(data)
B = random.choice(data)
while game_is_on:
    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}")
    print(art.vs)
    print(f"Against B: {B['name']}, {B['description']}, from {B['country']}")
    choice = input("Who has more followers? Type 'A' or 'B': ")
    max_followers = max(A['follower_count'], B['follower_count'])
    os.system('cls')
    print(art.logo)
    if (choice == 'A' and max_followers == A['follower_count']) or (
            choice == 'B' and max_followers == B['follower_count']):
        score += 1
        print(f"Awesome you are right. Current Score is {score}.")
        A = B
        B = random.choice(data)
    else:
        print(f"Sorry, You got it wrong! Your final score is {score}.")
        game_is_on = False
