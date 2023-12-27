from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def forward():
    tim.forward(100)


def backward():
    tim.backward(100)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkeypress(forward, "w")
screen.onkeypress(backward, "s")
screen.onkeypress(counter_clockwise, "a")
screen.onkeypress(clockwise, "d")
screen.onkeypress(clear_drawing, "c")
screen.exitonclick()
