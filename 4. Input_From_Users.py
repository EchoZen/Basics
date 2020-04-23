#Store the user input into a variable so it's usable
name= input("Enter your name:")
age= input("Enter your age:")
print("Hi " + name + "! You are " + age)

#Calculator app
#Python recognises inputs as strings, not numbers.
#You have to convert it to numbers for the calculator to work. Use a function.
num1= input("Enter a number:")
num2= input("Enter a number:")
#integer only allows integers for the calculation. Try it using a decimal. It won't work"
result= int(num1)+int(num2)
print(result)
#Using a float function allows decimal for the calculator
num1= input("Enter a number:")
num2= input("Enter a number:")
result= float(num1)+float(num2)
print(result)