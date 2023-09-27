from game_data import data
from art import logo
from art import vs
import random

def random_list_generator(_dt):
    return _dt

fail = True
score=0
while fail:
    _rand = random.randint(0, len(data) - 1)
    _rand2 = random.randint(0, len(data) - 1)
    if _rand==_rand2:
        _rand2 = random.randint(0, len(data) - 1)
    _dt = data[_rand]
    _dt2 = data[_rand2]
    print(_dt)
    print(logo)
    print(f"Compare A: {_dt['name']}, a {_dt['description']}, from {_dt['country']}")
    print(vs)
    print(f"Against B: {_dt2['name']}, a {_dt2['description']}, from {_dt2['country']}")
    guess=input("Who has more followers? Type 'A' or 'B':").lower()
    if guess == 'a':
        if _dt["follower_count"] > _dt2["follower_count"]:
            score += 1
            print(f"You're right! current score:{score}")
        else:
            fail=False
            print(f"Sorry, that's wrong. Final score:{score}")
    elif guess == 'b':
        if _dt2["follower_count"] > _dt["follower_count"]:
            score += 1
            print(f"You're right! current score:{score}")
        else:
            fail = False
            print(f"Sorry, that's wrong. Final score:{score}")

print(score)




