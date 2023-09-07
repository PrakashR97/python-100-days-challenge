#Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word=word_list[random.randint(0, len(word_list)-1)]
_chosen=[]
word=""


display=[]

for _ in range (len(chosen_word)):
    display+='_'
print(display)

guess=input("Guess a letter: ").lower()
for i in range (len(chosen_word)):
    if chosen_word[i]== guess:
       display[i]=guess
       _chosen.append(guess)
    else:
        print("wrong")
        _chosen.append("_")
print(word)
print(_chosen)
print(display)
