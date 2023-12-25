from turtle import Turtle, Screen

tim = Turtle()

for _ in range(15):
    tim.forward(10)
    tim.color("white")
    tim.forward(10)
    tim.color("black")

# other way can be to use penup() and pendown

screen = Screen()
screen.exitonclick()
