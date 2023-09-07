c='p'
x=ord(c)
#it will give you the ASCII value stored in x
print(x)
#it will return back the character


_word="hello"


def encrypt(shift,_word):
 _encode=""
 for i in range(len(_word)):
    _encode+=(chr(ord(_word[i])+shift))
 #_encode+=chr(ord(_word[i]))
 return _encode

def decrypt(shift,_word):
 _decode=""
 for i in range(len(_word)):
    # print(chr(ord(_word[i])-shift))
    _decode+=(chr(ord(_word[i])-shift))
 #_encode+=chr(ord(_word[i]))
 return _decode


text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))

print(encrypt(shift,text))
print(decrypt(shift,text))

