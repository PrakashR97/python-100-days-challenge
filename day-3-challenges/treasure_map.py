
_row1=['⬛','⬛','⬛']
_row2=['⬛','⬛','⬛']
_row3=['⬛','⬛','⬛']

x=[_row1,_row2,_row3]
print(f"{_row1}\n{_row2}\n{_row3}")
_treasure_point=input("Where do you to put the treasure?")
print(_treasure_point[0])
x[int(_treasure_point[1])-1][int(_treasure_point[0])-1]='X'

print(f"{_row1}\n{_row2}\n{_row3}")
