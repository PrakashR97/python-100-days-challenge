# import another_module
# from turtle import Turtle,Screen
#
# print(another_module.another_variable)
#
# tiny = Turtle()
# print(tiny)
# tiny.shape("turtle")
# tiny.color("coral")
# tiny.forward(100)
# tiny.left(90)
# tiny.forward(300)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "c"
table.padding_width = 10
table.header_style = "upper"
print(table)

