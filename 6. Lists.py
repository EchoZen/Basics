#List uses []. This lets you store multiple values
friends=["kevin", "mary", "benson", "richard", "stephen","mike"]
#Index:kevin=0, mary=1, benson=2
print(friends)
#To print a specific element using index,
print(friends[0])
print(friends[-1])
#To print a specific range of elements,
print(friends[1:])
print(friends[3:5])
print(friends[:5])
print(friends[1:6:2])

#Can also use a constructor to generate a list
aList= list("abc")
print(aList)
#This list contains 3 elements, ['a','b','c']

#Only lists can use sort function, so converting string to list is important
#Can use split, will make list based on white space
#Try to see it!
food= "apple pear orange strawberry"
mylist= food.split()
print(mylist)

#After that, can convert it back to string by joining it to empty string
#However, the white space will be removed
foodies= ''.join(mylist)
print(foodies)

#List comprehension
#syntactic structure for concise construction of lists.
#Try running it! Example:
print([n**2 for n in range(1,5)])
print([x+y for x in range(4,6) for y in range(1,5)])