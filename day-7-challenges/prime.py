import math

_num=int(input("?"))
i=2
_flag=False
for i in range(2,math.floor(_num/2)):
    if _num%i==0:
       _flag=True
       break

if not _flag:
    print(f"{_num} is a prime number")
else:
    print(f"{_num} is not a prime number")


