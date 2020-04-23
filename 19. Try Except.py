#Use it to catch errors in program
number= int(input("Enter a number:"))
print(number)
#Program with program: crashes if user enters a string or alphabet

try:
    number = int(input("Enter a number:"))
    print(number)
except:
    print("Invalid input")

#We can except specific errors
try:
    value= 10/0
    number = int(input("Enter a number:"))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")


