num1= float(input("Enter first number:"))
Op= input("Enter an operator:")
num2= float(input("Enter second number:"))

if Op== "+":
    print(num1+num2)
elif Op== "-":
    print(num1-num2)
elif Op== "/":
    print(num1/num2)
elif Op== "*":
    print(num1*num2)
else:
    print("invalid operator")