import random
import turtle as t

from hirst_painting import color_list

def drawing_dots():
 for j in range(1,10):
        tim.pendown()
        tim.color(random.choice(color_list))
        tim.dot(15)
        tim.up()
        tim.forward(40)
        tim.color(random.choice(color_list))
        tim.dot(15)
def move_left():
 tim.left(90)
 tim.forward(30)
 tim.left(90)

def move_right():
 tim.right(90)
 tim.forward(30)
 tim.right(90)

tim=t.Turtle()
t.colormode(255)

tim.left(180)
for i in range(1,5):

   drawing_dots()
   move_right()
   drawing_dots()
   move_left()

t.exitonclick()

