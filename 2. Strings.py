print("Ya boring")
#Backslash n puts the words behind it on a new line. Run the program!
print("Ya\nboring")
#Functions
Feeling= "i am bored and HAPPY!"
print(Feeling.lower())
print(Feeling.upper())
print(Feeling.title())
#Check if the sentence is title (Boolean)
print("I Am Back.")
print("I Am Back.".istitle())
#Can also check if it's alphabets, numbers, or alphanumberic
print("Iamback".isalnum())
#Check the length of the phrase
print(len("I am back"))
#There are 9 characters in "I am back". The first character starts with 0. So 0-8. From backwards, it's -1
phrase= "Elephant coconuts"
#This gives first index of the phrase
print(phrase[0])
print(phrase[5:15])
print(phrase[:10])
#This allows you to skip and alternate the indexes
print(phrase[0:20:2])
print(phrase[0:20:3])
#Finding first index number from letter
print(phrase.index("c"))
#Count number of letters
print(phrase.count("e"))
#Replace- string.replace(old, new, count)
#Count is for how many times you want to replace the old substring
phrase= "Elephant Elephant coconuts"
print(phrase.replace('Elephant', 'peanuts',1))
print(phrase.replace('Elephant', 'peanuts', 2))

#Combine sting or number with a comma (can be used for both strings and numbers
#+ can only be used to combine strings
#comma will add spacebar for concatenation naturally, while + doesn't
myName= '5'
print(myName)
print(myName+"is my favourite number")
print(myName, "is my favourite number")

#Using find() will count using the steps given
a= "Python Rules"
print(a[::-2].upper().find("Y"))
#The answer is not 1, but 5, cuz it counts from reverse, skipping by 2
