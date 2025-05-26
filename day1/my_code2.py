a=float(input("Enter num1: "))
b=float(input("Enter num2: "))
opr=input("Enter opr: ")
if opr=="+":
    c=a+b
if opr=="-":
    c=a-b
if opr=="*":
    c=a*b

print("result is ",c)

if a < 7:
    print("a is less that 7")
elif a == 7:
    print("a is equal to 7")
else:
    print("a is greater than 7")