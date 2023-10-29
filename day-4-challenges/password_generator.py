import random


#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# _pwd=""
# for i in range(0,nr_letters):
#    _letters=random.randint(0,len(letters)-1) #instead we can use random.choice(letters)
#    _pwd+=(letters[_letters])
#
# for i in range(0,nr_symbols):
#    _symbols=random.randint(0,len(symbols)-1)
#    _pwd+=(symbols[_symbols])
#
# for i in range(0,nr_numbers):
#    _numbers=random.randint(0,len(numbers)-1)
#    _pwd+=(numbers[_numbers])
#
# print(_pwd)
#
# # g^2jk8&P
# _randpassword=""
# _non_seq_pass=""
# for i in range (0,len(_pwd)):
#    _randpassword=random.randint(0,len(_pwd)-1)
#    _non_seq_pass+=_pwd[_randpassword]
#
# print(_non_seq_pass)


_pwd_list=[]
for i in range(0,nr_letters):
   _letters=random.randint(0,len(letters)-1) #instead we can use random.choice(letters)
   _pwd_list.append((letters[_letters]))

for i in range(0,nr_symbols):
   _symbols=random.randint(0,len(symbols)-1)
   _pwd_list.append(symbols[_symbols])

for i in range(0,nr_numbers):
   _numbers=random.randint(0,len(numbers)-1)
   _pwd_list.append(numbers[_numbers])



random.shuffle(_pwd_list)


# g^2jk8&P
final_pwd=""
for i in _pwd_list:
   final_pwd+=i

print(f"Your password in {final_pwd}")

