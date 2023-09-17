################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

#Global Scope
player_health=10

# def game():
#     def drink_potion():
#       player_health=2
#       print(player_health,"Prakash")
#     drink_potion()
#
# game()

# In python, There is no Block Scope

# if 3>2:
#     a_var=10


# if we create variable within function that means local scope
# if we create variable within if block,while block that means it is not local scope

#
# game_level=3
# def create_enemy():
#  enemies = ["Skeleton", "Zombie", "Alien"]
#  if game_level<5:
#         new_enemy=enemies[0]
#
# print(new_enemy)


# Modifying Global Scope
enemies=1

# def increase_enemies():
#  global enemies
#  enemies+=1
#  print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

#Global Constants

PI=3.14159
URL="https://www.google.com"
