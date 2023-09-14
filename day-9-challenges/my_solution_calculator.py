

def div(n1,n2):
    return  n1/n2

def sub(n1,n2):
    return  n1-n2

def mul(n1,n2):
    return  n1*n2

def add(n1,n2):
    return  n1+n2

con=True


operations={"+":add,
            "-":sub,
            "/":div,
            "*":mul}

num1=int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)

operation_symbol=input("Pick an operation from the line above")
# answer=0
# for i in operations:
#     print(i)
#     if i==operation_symbol:
#         answer=operations[i](num1,num2)
num2=int(input("What's the second number?: "))
calculation_function=operations[operation_symbol]
first_answer=calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")
while con:
 operation_symbol=input("Pick another operation: ")
 num3=int(input("What's the next number?: "))
 calculation_function=operations[operation_symbol]
 second_answer=calculation_function(first_answer,num3)
 print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
 yes_or_no=input(f"Type 'y' to continue calculation with {second_answer}, or type 'n' to exit.:")
 first_answer=second_answer
if yes_or_no=="n":
    con=False