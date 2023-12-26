from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ["purple", "medium violet red", "chartreuse", "dark green", "teal", "cyan", "navy", "firebrick"]
directions = [0, 90, 180, 270]
tim.pensize(5)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
