# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# def encrypt(text,shift):
#  encode=""
#  for i in range(len(text)):
#     # if alphabet.index(i)>0:
#
#      encode+=alphabet[alphabet.index(text[i])+shift]
#
#  return encode
#
# print(encrypt(text,shift))
#
#

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter
#   print(f"The encoded text is {cipher_text}")

# def decrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter
#   print(f"The encoded text is {cipher_text}")
#
# if direction=="encode":
#  encrypt(plain_text=text, shift_amount=shift)
# elif direction=="decode":
#  decrypt(plain_text=text, shift_amount=shift)


def ceaser(plain_text, shift_amount,direction):
   cipher_text = ""
   for letter in plain_text:
     position = alphabet.index(letter)
     if direction=="encode":
      new_position = position + shift_amount
     elif direction=="decode":
       new_position = position - shift_amount
     new_letter = alphabet[new_position]
     cipher_text += new_letter
   print(f"The encoded text is {cipher_text}")

ceaser(text,shift,direction)


