from turtle import Screen, Turtle
import random


def setup_writers(x, y):
    """This function setup all writers that will write on turtle screen."""
    writer_main = Turtle()
    writer_main.penup()
    writer_main.hideturtle()
    writer_main.setpos(x=x, y=y)

    return writer_main


def write_champions_info(champ):
    writer = setup_writers(-90, 170)
    writer.write(f"Gold: {champ[0].pencolor()} won!", False, align="center",
                 font=('Arial', 14, 'normal'))

    writer = setup_writers(-90, 140)
    writer.write(f"Silver: {champ[1].pencolor()}!", False, align="center",
                 font=('Arial', 14, 'normal'))

    writer = setup_writers(-90, 110)
    writer.write(f"Bronze: {champ[2].pencolor()}!", False, align="center",
                 font=('Arial', 14, 'normal'))


is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
race_participants = []
for color in colors:
    race_participants.append(Turtle(shape="turtle"))

y = -100
for indeks, turt in enumerate(race_participants):
    turt.penup()
    turt.color(colors[indeks])
    turt.goto(x=-238, y=y)
    y += 35

is_race_on = True
count = 0
champions = []
turts_to_remove = []

while is_race_on:
    # Movement
    for turt in race_participants:
        move_forward = random.randint(1, 10)
        turt.forward(move_forward)

    # Checking if turtle won.
    for index, turt in enumerate(race_participants):
        if turt.xcor() > 200:
            count += 1
            champions.append(turt)
            turts_to_remove.append(index)
            if count > 3:
                write_champions_info(champions)
                is_race_on = False

    # We remove from checking and moving list those turtles that already finish race.
    counter = 1
    for i, champ in enumerate(turts_to_remove):
        if i == 0:
            race_participants.pop(champ)
        else:
            champ -= counter
            race_participants.pop(champ)

        counter += 1

    turts_to_remove.clear()

screen.exitonclick()