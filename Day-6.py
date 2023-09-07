
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

_seq=0
while not display.index("_") and _seq<word_length:
    print("1")
    _seq+=1


_=["a","a","s"]

print(list(chosen_word))