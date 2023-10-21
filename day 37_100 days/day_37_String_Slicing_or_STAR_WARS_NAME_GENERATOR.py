# Slice it Up!
# May the force be with you as you slice it up! Create your Star Wars name with string slicing.


# What is your Star Wars name? Check mine out! Day 37 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python





# print("String Slicing")
# print()

# myString = "Hellow there my friend!"
# print(myString[0:5])
# print()

#________________________________________________

# print("The Secret Third Argument")
# print()

# myString = "Hellow there my friend!"
# print(myString[::-1])

#_______________________________________________________________________

# print("Split")
# print()
'''👉 split lets us split a string into a list of individual words by separating it at the space characters.'''

# myString = "Hellow there my friend!"
# print(myString.split())


#_______________________________________________________________________

# print("Common Errors")
# print()


'''
It stops printing too early

👉 Why is it printing 'Hell' instead of 'Hello'?

myString = "Hello there my friend."
print(myString[0:4])'''

# myString = "Hello there my friend."
# print(myString[0:5])

'''It won't stop printing the same character

👉 What is the problem here?

myString = "Hello there my friend."
print(myString[0:4:0])

'''
# myString = "Hello there my friend."
# print(myString[0:5])

#_______________________________________________________________________

# print("Fix My Code")
# print()

'''# This code should output 'Hello there'
myString = "Hello there my friend."
print(myString[0:10:0])'''


# This code should output 'Hello there'
# myString = "Hello there my friend."
# print(myString[0:11])


#_______________________________________________________________________

print("👉 Day 37 Challenge")
print()

print("STAR WARS NAME GENERATOR")

all = input("Enter your first name, last name, Mum's maiden name and the city you were born in >> ").split()

first = all[0].strip()
last = all[1].strip()
maiden = all[2].strip()
city = all[3].strip()

# first = input("First Name > ").strip()
# last = input("Last Name > ").strip()
# maiden = input("Mum's maiden Name > ").strip()
# city = input("city where you born > ").strip()

name = f"{first[:3].title()}{last[:2].lower()} {maiden[:2].title()}{city[-3:].lower()}"
print("your star wars name is : ", name)






#replit100DaysOfCode