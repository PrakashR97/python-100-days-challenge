from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()


def move_forward():
    tim.forward(10)


screen.onkey(key="a", fun=move_forward)
screen.exitonclick()
