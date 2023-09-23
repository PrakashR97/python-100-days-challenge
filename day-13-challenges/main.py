from game_data import data
from art import logo
from art import vs
import random

def random_list_generator(_dt):
    return _dt

fail=True
score=0
while fail:
    _rand = random.randint(0, len(data) - 1)
    _rand2 = random.randint(0, len(data) - 1)
    _dt = data[_rand]
    _dt2 = data[_rand2]
    print(_dt)
    print(logo)
    print(f"Compare A: {_dt['name']}, a {_dt['description']}, from {_dt['country']}")
    print(vs)
    print(f"Against B: {_dt2['name']}, a {_dt2['description']}, from {_dt2['country']}")
    _one = _dt["follower_count"]
    _two = _dt2["follower_count"]
    print(_one,_two)
    _input=input("Who has more followers? Type 'A' or 'B':").lower()
    if _input=='a' :
        if _one > _two:
            score+=1
            print(f"You're right! current score:{score}")
        else:
            fail=False
            print(f"Sorry, that's wrong. Final score:{score}")
    elif _input=='b':
        if _two > _one:
            score+=1
            print(f"You're right! current score:{score}")
        else:
            fail=False
            print(f"Sorry, that's wrong. Final score:{score}")

print(score)




