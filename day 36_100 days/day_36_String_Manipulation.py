# That's Not My Name...
# That's not my name...Learn how string manipulation can improve your 'if' statements.


# Did I forget your name?!...Check out my contact list. Day 36 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python


# print("String Manipulation")
# print()
'''
    .lower = all letters are lower case
    .upper = all letters are upper case
    .title = capital letter for the first letter of every word
    .capitalize = capital letter for the first letter of only the first word
'''

'''.strip() removes any spaces on either side of the word.'''

# name = input("What is your Name?")
# if name.lower().strip() == "david":
#   print("Hello David")
# else:
#   print("what a beautyful head of hair!")
# ________________________________________________________________________

# print("No Duplicates")
# print()

# myList = []

# def printList():
#   print()
#   for i in myList:
#     print(i)
#   print()

# while True:
#   addItem = input("Item > ").capitalize().strip()
#   if addItem not in myList:
#     myList.append(addItem)
#   printList()


# _________________________________________________________________________________________________


# print("Common Errors")
# print()

'''myList = []

def printList():
 print()
 for i in myList:
   print(i)
 print()

while True:
 addItem = input("Item > ").capitalize().strip()
 if addItem not in myList:
   myList.append(addItem)
 printList()'''

# myList = []

# def printList():
#  print()
#  for i in myList:
#    print(i)
#  print()

# while True:
#  addItem = input("Item > ").strip().capitalize()
#  if addItem not in myList:
#    myList.append(addItem)
#  printList()


# _________________________________________________________________________________________________


# print("Fix My Code")
# print()

'''whatToEat = input("What do you fancy for dinner? ")
if whatToEat.strip = "pasta": 
  print("Get out the pasta maker.")
elif whatToEatlower() == "TACOS":
  print("Let's do Taco Tuesday!")
else: 
  print("Go search the fridge.")'''

# whatToEat = input("What do you fancy for dinner? ")
# if whatToEat.strip().lower() == "pasta":
#   print("Get out the pasta maker.")
# elif whatToEat.strip().lower() == "tacos":
#   print("Let's do Taco Tuesday!")
# else:
#   print("Go search the fridge.")


# _________________________________________________________________________________________________


print("👉 Day 36 Challenge")
print()

nameList = []


def printList():
    print()
    for i in nameList:
        print(i)
    print()


while True:

    firstName = input("Enter your First Name > ").strip().capitalize()
    lastName = input("Enter your Last Name > ").strip().capitalize()
    name = f"{firstName} {lastName}"
    if name not in nameList:
        nameList.append(name)
    else:
        print("ERROR: Duplicate name")
    printList()




#replit100DaysOfCode