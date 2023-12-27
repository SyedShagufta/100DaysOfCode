from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? (Red, Blue, Green, Yellow, Purple, Orange) Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)


def draw_finish_line():
    tim = Turtle()
    tim.hideturtle()
    tim.penup()
    tim.pencolor("black")
    tim.pensize(5)
    tim.goto(230, 200)
    tim.pendown()
    tim.right(90)
    tim.forward(400)


if user_bet:
    is_race_on = True
    draw_finish_line()

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've Won! The {winning_turtle} turtle is the winner.")
            else:
                print(f"You've Lost! The {winning_turtle} turtle is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()