#To use a function, you need to type def
#All the code after the colon is part of the function. The code must be indented.
#Any code not indented is not part of the function.
#The () lets you specify a parameter (an input).
name= input("Enter your name:")
age= input("Enter your age:")
def say_hi(name, age):
    print("Hello " + name+ ", you are "+ age)
#The program won't print hello user until you call the function
say_hi(name, age)
say_hi("Lisa", "89")

#Return statement, lets you get back output
def cube(num):
    return num*num*num

#Whatever that comes after the return (even if it's indented) will not be part of the function 
result= cube(4)
print(result)