# my_solution

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"
_seq=0
while display.count("_")>0 and _seq<word_length:
    if display.count("_") > 0 and _seq >= word_length:
        print("You loose")
    print("1")
    _seq+=1
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
     letter = chosen_word[position]
     print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
     print(display.count(letter),[chosen_word].count(letter))
     if letter == guess and display.count(letter)<=list(chosen_word).count(letter):
        display[position] = letter
     print(display)
    if  display.count("_")==0:
        print("You won")
        break





















