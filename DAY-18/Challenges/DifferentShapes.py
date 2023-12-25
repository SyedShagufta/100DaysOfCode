import random
from turtle import Turtle, Screen

tim = Turtle()

colors = ["red", "blue", "green", "yellow", "purple"]


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)


for shape_side in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side)

screen = Screen()
screen.exitonclick()
