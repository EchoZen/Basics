#Use extend function to append two lists together
lucky_numbers= [0,400,30,700,67,92]
friends= ["kevin", "mary", "benson", "richard", "stephen","mike"]
friends.extend(lucky_numbers)
print(friends)
#Use append to add another item to the list. (Can only add at the end)
lucky_numbers.append(90)
print(lucky_numbers)
#Remove the item from the list
friends.remove("mary")
print(friends)
#Use insert to add the item in a specific position
friends.insert(1, "mark")
print(friends)
#Find the index of an element in the list
print(friends.index("mark"))
#Count the number of elements in the list
print(friends.count("mary"))
#Sort the list in ascending order
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
#Copy a list
friends2= friends.copy()
print(friends2)
#Clear the entire list
friends2.clear()
print(friends2)
