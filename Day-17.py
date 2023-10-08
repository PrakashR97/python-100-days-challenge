import turtle as t
import heroes
import pandas

tim = t.Turtle()

# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
for _ in range(4):
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)


for _ in range(10):
    t.right(72)
    t.forward(100)
    t.right(72)
    t.forward(100)
t.forward(10)
for _ in range(10):
    t.right(72)
    t.forward(120)
    t.right(72)
    t.forward(120)
t.forward(10)
for _ in range(10):
    t.right(72)
    t.forward(140)
    t.right(72)
    t.forward(140)



t.exitonclick()


# import random
# import turtle as t
#
# tim = t.Turtle()
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# degree = 360
# sides = 3
# angel = degree / sides
# test = True
# while test:
#     angel = degree / sides
#     for _ in range(sides):
#         t.color(random.choice(colours))
#         t.forward(100)
#         t.right(angel)
#     sides += 1


import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]

"""
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    tim.speed(9)
    tim.pen( pensize=10)
    draw_shape(shape_side_n)"""

import turtle as t
import random

tim = t.Turtle()


# directions = [tim.right, tim.left, tim.right, tim.left, tim.right, tim.left]
#
# for i in range(1000):
#     tim.color(random.choice(colours))
#     tim.pensize(5)
#     tim.speed(10)
#     tim.forward(20)
#     selected_direction = random.choice(directions)
#     selected_direction(90)
#
# t.exitonclick()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


#
#
# print(type(random_color()))
# t.colormode(255)
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# for _ in range(100):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
# t.exitonclick()
angle = 5
t.colormode(255)
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)