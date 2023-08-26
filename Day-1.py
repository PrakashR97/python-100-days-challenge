
# input function
#name = input('Please enter your name: ')
#print(name)

#String
"Hello"[2]
print("Hello"[2])

#Integer
print(123+234)
123_456_666
print(123_456_666)
#123456666

#Float
3.14159
print(3.14159)

#Boolean
True
False

#Type Error, Type Checking and Type Conversion

print(len("prakash"))
#print(len(123))

num_char=len(input("what is your name?"))
print(num_char)
#string conversion
new_num_char=str(num_char)
print("Your name has "+new_num_char+" characters")

#Type Checking
a=123
print (type(a))

a_f=float(123)
print(type(a_f))

#Mathetical operations

3+5
7-4
3*2
6/3
2**4 #2 to the power of 4
#PEMDAS Rule
#PEMDAS stands for Parentheses, Exponents, Multiplication and Division (same level), and Addition and Subtraction (same level).
#multiline comment
"""
()
**
*/
+-
"""
print(3*(3+3)/3-3)

#Number manipulation
print(round(8/3,1))



7/4  #floating point number
7//6 #integer number


score=0
height=1.8
isWinning=True

#f-string
print(f"your scoure is {score}, your height is {height}, you are winning is {isWinning}")




age=input("what is your current age ?")


print(type(age))
rest_age_to_live=100-int(age)


days=(rest_age_to_live*365)

weeks=days/7

#g
months=days/30


print(F"You have {days} days, {weeks} weeks, and {months} months left.")



