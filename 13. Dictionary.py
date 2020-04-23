# Use {} for dictionary
# variable= {"key":"value", "key":"value"...}
#1key:value is considered as 1 element in the dictionary
# To access value in variable, you can use the key
monthConversions= {"Jan": "January",
                   "Feb": "February",
                   "Mar": "March",
                   "Apr": "April",
                   "May": "May",
                   "Jun": "June",
                   "Jul": "July",
                   "Aug": "August",
                   "Sep": "September",
                   "Oct": "October"}
#1st way to retrieve value
print(monthConversions["Mar"])
#2nd way
print(monthConversions.get("Oct"))
'''Good way of using get lets you know if your key is not mappable to any values in the dictionary,
by adding a comma and a string. eg. monthConversions.get("invalid key", "insert something to let you know it 
is an invalid key)'''
print(monthConversions.get("Aug", "birdwatching"))
print(monthConversions.get("Long", "birdwatching"))
#By putting something behind the comma, it prints that out if the key is not in the dictionary.

#Keys must be immutable- can be strings, integers or tuples
#Values can be anything
#Dictionaries are mutable
mydict={}
mydict['bill']= 25
mydict['sun']="moon"
print(mydict)
print(mydict.items())
print(mydict.keys())
mydict.update(monthConversions)
print(mydict)