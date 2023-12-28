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
    tim = Turtle("square")
    tim.penup()
    tim.speed("fastest")
    tim.pencolor("black")
    tim.pensize(5)
    x = 200
    y = 180
    for _ in range(9):
        tim.goto(x, y)
        tim.stamp()
        x += 20
        y -= 20
        tim.goto(x, y)
        tim.stamp()
        x -= 20
        y -= 20
        tim.goto(x, y)
        tim.stamp()


if user_bet:
    is_race_on = True
    draw_finish_line()

writer = Turtle()
writer.hideturtle()
writer.home()
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                writer.write(f"You Won! The {winning_turtle} turtle is the winner.", False, align="center",
                             font=('Arial', 14, 'normal'))
                print(f"You've Won! The {winning_turtle} turtle is the winner.")
                break
            else:
                writer.write(f"You've Lost! The {winning_turtle} turtle is the winner.", False, align="center",
                             font=('Arial', 14, 'normal'))
                print(f"You've Lost! The {winning_turtle} turtle is the winner.")
                break
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
