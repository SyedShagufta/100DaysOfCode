# import colorgram
#
# colors = colorgram.extract("image.jpg", 6)
#
# colorList = []
#
# for i in range(len(colors)):
#     t = (colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b)
#     colorList.append(t)

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colorList = [(253, 253, 249), (240, 254, 247), (253, 244, 251), (235, 239, 252), (40, 7, 178), (87, 248, 180)]
tim.setheading(255)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(colorList))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(58)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
