from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)


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


draw_finish_line()
screen.exitonclick()
