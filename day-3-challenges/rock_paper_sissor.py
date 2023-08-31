import random

#Write your code below this line 👇



_in=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

r_p_s=["rock","paper","scissors"]

_rand=random.randint(0,len(r_p_s)-1)


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

r_p_s=[rock,paper,scissors]
n=5
while n>0:
    if _in>=3 or _in<0:
        print("you typed an invalid number, you lose!")
        break
    if _in==_rand:
        print("Draw")
        break;
    elif _in==0 and _rand==2:
        print(f"you won!! \nyou picked \n{r_p_s[_in]} \nOpponent picked \n{r_p_s[_rand]}")
        break
    elif _in==1 and _rand==0:
        print(f"you won!! \nyou picked \n{r_p_s[_in]} \nOpponent picked \n{r_p_s[_rand]}")
        break
    else:
        r_p_s[_rand]
        print(f"you loose!! \nyou picked \n{r_p_s[_in]} \nOpponent picked \n{r_p_s[_rand]}")
        break

#better version
'''
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
else:
    print("It's a draw")
'''


