# import random
#
# _ran_integer=random.randint(0.0,5)
# print(_ran_integer)
#
# love_score=random.randint(1,100)
# print(f"Your love score is {love_score}")


#List

states_of_america=['Bloomingdale',
'Capitol Hill',
'Cathedral Heights',
'Chinatown',
'Columbia Heights',
'Dupont Circle',
'Edgewood',
'Georgetown',
'Logan Circle',
'Navy Yard'
]

states_of_america[-1]='New Yard'
states_of_america.append("Pennsylvania")
states_of_america.extend(["PrakashLand","Columbia"])
print(states_of_america)

'''
handling index errors
'''

print(states_of_america[len(states_of_america)-1])



# dirty_dozen=["Strawberries",
# "Spinach",
# "Kale", "collard", "mustard greens.",
# "Peaches.",
# "Pears.",
# "Nectarines.",
# "Apples.",
# "Grapes."]

fruits=["Peaches",
"Pears",
"Nectarines",
"Apples",
"Grapes","Strawberries"]

vegetables=["Spinach",
"Kale", "collard", "mustard greens"]

'''
nested list
'''

dirty_dozen=[vegetables,fruits]
print(dirty_dozen)

print(dirty_dozen[0][2])