
is_male= True
if is_male:
    # If the condition is true, anything below with indentation will be executed
    print("You are a male")

is_male= False
if is_male:
    #Since is_male is now false, the program is not executed and nothing happens.
    print("You are a male")
    #How to know if the program is running if nothing happens? Use else
else:
    print("You are not a male")

#We can make the program more complex with relational operators (and, or, not)
is_male= False
is_tall= True
#Try changing the booleans and see what you get!
if is_male or is_tall:
    print("You are male or tall or both.")
else:
    print("You are neither male nor tall")
#Use not() to test if you want to execute a function when the condition is not true!
if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not(is_tall):
    print("You are a short male.")
elif not(is_male) and is_tall:
    print("You are tall but not male")
else:
    print("You are neither male nor tall")