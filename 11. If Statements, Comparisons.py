#Operators
#= always come after. NOTE: IF ONLY USE = it would be specifying variable, not comparing
# >, <, ==, >=, <=, != (not equal)

#Build a function that chooses the biggest number
def maxnum(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num3:
        return num2
    else:
        return num3
print(maxnum(100,40,5))