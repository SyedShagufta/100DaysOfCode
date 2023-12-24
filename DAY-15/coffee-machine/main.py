from data import resources
from data import MENU

PROFIT = 0


def print_report():
    print(f"Water  : {resources['water']}ml")
    print(f"Milk   : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money  : ${PROFIT}")


def enough_resources(coffee):
    ingredients = MENU[coffee]["ingredients"]
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
        else:
            return True


def use_resources(coffee):
    ingredients = MENU[coffee]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]


def transaction_success(money, coffee):
    global PROFIT
    cost = MENU[coffee]["cost"]
    change = money - cost
    if change > 0:
        print(f"Here is ${change} in change.")
        PROFIT += cost
        return True
    elif change == 0:
        PROFIT += cost
        return True
    else:
        return False


def press_coins(coffee):
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    money = round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)
    if transaction_success(money, coffee):
        print(f"Here is your {coffee} ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


def make_coffee(coffee):
    if coffee == "espresso" or coffee == "latte" or coffee == "cappuccino" and enough_resources(coffee):
        print("Please insert coins")
        press_coins(coffee)
        use_resources(coffee)
    else:
        print("Choose a Valid Response!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report()
    else:
        make_coffee(choice)
