import turtle as t
from random import choice

import colorgram
# 
# rgb_colours = []
# colours = colorgram.extract('image.jpg', 25)
# for color in colours:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colortuple = (r, g, b)
#     rgb_colours.append(colortuple)
# print(rgb_colours)
#we got the color datas from the picture below

colour_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
               (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
               (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
               (19, 86, 89), (82, 148, 129), (147, 17, 19)]
t.colormode(255)


def create_circle(drawer):
    z = 0

    for _ in range(26):

        for i in range(30):
            drawer.dot(15, choice(colour_list))
            drawer.forward(30)

        if z % 2 == 0:
            drawer.dot(15, choice(colour_list))
            drawer.left(90)
            drawer.forward(30)
            drawer.left(90)
        else:
            drawer.dot(15, choice(colour_list))
            drawer.right(90)
            drawer.forward(30)
            drawer.right(90)
        z += 1


esek = t.Turtle()
esek.speed("fastest")
esek.hideturtle()
esek.penup()
esek.goto(-450,-375)
create_circle(esek)

ekran = t.Screen()

print(ekran.canvheight)

ekran.exitonclick()
