#
for letter in "Giraffe Academy":
    print(letter)

#Can also be used for arrays
friends= ["Jim", "Karen", "Michael"]
for friend in friends:
    print(friend)

#Can also be used for numbers
for number in range(5,15): #does not include 15
    print(number)

#Can also use indexes to print all the elements in the list
friends= ["Jim", "Karen", "Michael"]
for index in range(len(friends)):
    print(friends[index])