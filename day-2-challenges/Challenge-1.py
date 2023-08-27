
name1 = input("What is your name?")
name2 = input("What is their name?")


n1_n2=name1+name2

_true=0
_love=0

for i in range(len(n1_n2)):
    if(n1_n2[i].upper() in('T','U','R','E')):
        _true+=1
    if(n1_n2[i].upper() in('L','O','V','E')):
        _love+=1

_score=int(str(_true)+str(_love))

print(_score)


if _score<=10 or _score>=90:
    print(f"Your score is {_score}, you go together like coke and mentos.")
elif _score>40 and _score<50:
    print(f"Your score is {_score}, you are alright together.")
else:
    print(f"Your score is {_score}")




