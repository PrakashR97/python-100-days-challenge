import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
# user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -70, -40, -10, 20, 50]

for i in range(0,6):
    tim=Turtle(shape="turtle")
    tim.color(color[i])
    tim.penup()
    tim.goto(x=-230,y=y_position[i])


screen.exitonclick()
