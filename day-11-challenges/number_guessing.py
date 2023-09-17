import random



print("Welcome to the NUmber Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level=input("Choose a difficulty. Type 'easy' or 'hard':")

chance=0
if level.lower()=='easy':
    chance=10
if level.lower()=='hard':
    chance=5

guessing_number=random.randint(1,100)
print(guessing_number)
fail=True
while fail:
    guess=int(input("Make a guess: "))
    if guessing_number<guess:
        chance-=1
        print("Too high")
        print("Guess again.")
        if chance ==0:
            print("You loose!")
            print(f"Your guessing number is {guessing_number}")
            fail=False
        print("Guess again.")
        print(f"You have {chance} to guess the number")
    if guessing_number > guess:
        chance -= 1
        print("Too low")
        if chance ==0:
            print("You loose!")
            print(f"Your guessing number is {guessing_number}")
            fail=False
        print("Guess again.")
        print(f"You have {chance} to guess the number")
    if guessing_number == guess:
        print("You Win!")
        print(f"Your guessing number is {guessing_number}")
        fail=False