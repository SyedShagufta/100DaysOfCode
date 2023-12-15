import data

print(data.palace)
print("Welcome to the Enchanted Palace, where hidden secrets await. Your mission is to uncover the ancient artifact "
      "rumored to hold unimaginable power.")
choice = input("Left or Right?").lower()
if choice == "right":
    print("You fall into the hole. Game over.")
elif choice == "left":
    choice_1 = input("Swim or Wait").lower()
    if choice_1 == "swim":
        print("Attacked by trout. Game Over.")
    elif choice_1 == "wait":
        choice_2 = input("Which door? Red, Blue or Yellow ?").lower()
        if choice_2 == "blue":
            print("Attacked by beasts. Game Over.")
        elif choice_2 == "red":
            print("Burned by Fire. Game Over.")
        elif choice_2 == "yellow":
            print("You Win 🏆 !")
        else:
            print("Game Over.")
    else:
        print("Wrong choice, Game Over buddy.")
else:
    print("Wrong Choice, Game Over.")
