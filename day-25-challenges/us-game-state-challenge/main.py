import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.tracer(0)

game_is_on = True


def get_state_coordinates(state):
    data = pandas.read_csv("50_states.csv")
    state_cor = data[data["state"] == state]
    print(state_cor)
    x = 0
    y = 0
    for i in state_cor.x:
        x = i
    for i in state_cor.y:
        y = i
    return x, y


while game_is_on:
    turtle.goto(0, 0)
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    turtle.goto(get_state_coordinates(answer_state))
    turtle.write(answer_state)
turtle.exitonclick()
turtle.mainloop()
