print("Welcome to Treasure Island Your mission is to find find the reasure")
_l_r=input("Do you want to go left or right?")

if _l_r=="left":
    _s_w=input("Do you want to swim or wait?")
    if _s_w=="wait":
     _w_d=input("Which door you want to open?")
     if _w_d=="red":
           print("Burned by fire. Game Over!!")
     elif _w_d=="blue":
           print("Eaten by beasts. Game Over!!")
     elif  _w_d=="yello":
           print("You Win!")
     else:
         print("Game Over!!!")
    else:
        print("Attacker by trout. Game Over!!")
else:
    print("Fall into a hole Game Over!!")