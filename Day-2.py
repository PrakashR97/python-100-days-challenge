print("Welcome to the rollercoaster!")


height=int(input("What is is your height in cm?"))

#if statement
if height>120:
    print("You can ride the rollercoaster")
else:
    print("Sorry, you have to grow taller before you can ride")

#odd or even
num=43
if(num%2==0):
    print("even")
else:
    print("odd")


#nested if statement

age=int(input("Please enter your age?"))
if height>120:
 if age<12:
    print("Please pay 5$")
 elif age<=18           :
    print("Please pay 12$")
 else:
     print("Please pay 18$")
else:
    print("Sorry, you have to grow taller before you can ride")

#
height1=float(input("enter your height in m: "))
weight1=float(input("enter your weight in kg: "))

bmi=weight1/(height1**2)
if bmi<18.5:
    print(f"your bmi is {bmi}, you are underweight")
elif bmi<25:
    print(f"your bmi is {bmi}, you are normal weight")
elif bmi<30:
    print(f"your bmi is {bmi}, you are over weight")
else:
    print(f"your bmi is {bmi}, you are clinically obese")

#leap year

leap_year_or_not=int(input("pls enter year"))
year=leap_year_or_not
if year%4==0:
    if year%100!=0:
        print("leap year")
    elif year%400==0:
        print("leap year")
    else:
        print("not leap year")
else:
    print("not leap year")

_dollar=0


if height>120:
 print("You can ride the rollercoaster!")
 if age>=45 and age<=50:
     _dollar+=0
     print("Everything is going to be ok. Have a ride on us")
 elif age<12:
    _dollar+=5
    print(f"Child tickets are ${_dollar}")
 elif age<18:
    _dollar+=7
    print(f"Youth tickets are ${_dollar}")
 else:
    _dollar+=12
    print(f"Adult tickets are ${_dollar}")
 y_n=input("Do you want a photo taken? Y or N")
 if y_n.upper()=="Y":
       print(f"Your final bill is ${_dollar+3}")
 else:
       print(f"Your final bill is ${_dollar}")
else:
   print("Sorry, you have to grow taller before you ride.")


# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

_pizza=0
_pepperoni=0
_bill=0
pizza_size=(input("Which size pizza you want?"))
if pizza_size.upper()=='S':
  _pizza=15
  _bill+=_pizza
if pizza_size.upper()=='M':
  _pizza=20
  _bill+=_pizza
if pizza_size.upper()=='L':
  _pizza=25
  _bill+=_pizza

_pepperoni_size=(input("Which size pepperoni you want?"))
if _pepperoni_size.upper()=='S':
  _pepperoni=2
  _bill+=_pepperoni
if (_pepperoni_size.upper()=='M'or _pepperoni_size.upper()=="L"):
  _pepperoni=3
  _bill += _pepperoni

_extra_cheese=input("Do you want extra cheese?")
if _extra_cheese.upper()=="Y":
    _bill+=1

print(f"your final bill is ${_bill}")


bill=0
size=(input("Which size pizza you want?"))
if size=="S":
    bill+=15
elif size=='M':
    bill+=20
else:
    bill+=25

_pepperone_add=(input("Do you want add pepperoine?"))

if _pepperone_add=='Y':
    if size=='S':
        bill+=2
    else:
        bill+=3

_cheese_add=(input("Do you want add cheese?"))

if _cheese_add=='Y':
    bill+=1

print(f"Your final bill is ${bill}")




