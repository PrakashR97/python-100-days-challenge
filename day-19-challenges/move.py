from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_up():
    new_heading = turtle.heading() + 90
    turtle.penup()
    turtle.setheading(new_heading)


def move_left():
    new_heading = turtle.heading() + 180
    turtle.penup()
    turtle.setheading(new_heading)


def move_right():
    new_heading = turtle.heading() + 0
    turtle.penup()
    turtle.setheading(new_heading)


def move_down():
    new_heading = turtle.heading() + 270
    turtle.penup()
    turtle.setheading(new_heading)


screen.listen()
screen.onkey(move_up, 'Up')
screen.onkey(move_down, 'Down')
screen.onkey(move_left, 'Left')
screen.onkey(move_right, 'Right')

turtle.forward(10)
screen.exitonclick()
