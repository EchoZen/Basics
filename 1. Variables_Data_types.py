# This is a way you can comment
'''This is also a comment. It does not affect the program'''
#Data_types: Strings, numbers, boolean value(true, false)
#STRINGS
#These are all valid ways to type a string. For more multiple lines, use triple '''
print("Hi Zoe")
print('Hi Zoe')
print('''Hi
Zoe''')

#NUMBERS
#For numbers, you can add, substract, multiply and divide. Try changing the numbers and running the program!
#There is no need for ''
print(2+2)
print(7*9)
#Dividing the number gives you a float. (Result has decimal point)
print(6/3)
#To get rid of the float, use integer function. (doesn't round up or down, just truncates value)
print(int(21/7))
#You can also // to get rid of float
print(21//7)
#Cannot divide by 0. Will give error.

#BOOLEAN
#For boolean data type, F and T is always capital. If not, it becomes a variable
is_male= True
is_tall= False

#VARIABLES
#Lets you modify the program easily. Change the names and run the program!
name= "Martha"
#variables + strings are called contatenation.
print(name + " loves to eat.")
print("Zoe is " + name + "'s best friend.")
#You can also change the variable halfway through the program.
name= "John"
print(name + "'s favourite sport is minigolf.")
print(name + "'s favourite food is sushi.")
