# Dictionaries are Back...
# That can only mean one thing! The return of 'MokeBeasts.' But, first let's tackle 2D dictionaries with another game that may or may not include a candlestick, the library...


# MokeBeasts are back! Day 46 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python




# print("2D Dictionaries")
# print()
# print("Dynamically Adding To A 2D Dictionary")
# print()

# clue = {}

# while True:
#   name = input("Name: ")
#   location = input("Location: ")
#   weapon = input("Weapon: ")

#   clue[name] = {"location": location, "weapon":weapon}
#   print(clue)

# print("Pretty Printing")
# print()
'''👉 This example shows you how to add a prettyPrint() subroutine that works with a 2D dictionary.'''

# def prettyPrint():
#   print()
#   for key, value in clue.items():
#     print(key, end=": ")
#     for subKey, subValue in value.items():
#       print(subKey, subValue, end=" | ")
#     print()


'''When combined with the 2D dictionary code:'''


# clue = {}
# def prettyPrint():
#   print()

#   for key, value in clue.items():
#     print(key, end=": ")
#     for subKey, subValue in value.items():
#       print(subKey, subValue, end=" | ")
#     print()

# while True:
#   name = input("Name: ")
#   location = input("Location: ")
#   weapon = input("Weapon: ")

#   clue[name] = {"location": location, "weapon":weapon}

#   prettyPrint()



#___________________________

# print("Accessing a Single Item")
# print()

# john = {"daysCompleted": 46, "streak": 22}
# janet = {"daysCompleted": 21, "streak": 21}
# erica = {"daysCompleted": 75, "streak": 6}

# courseProgress = {"John":john, "Janet":janet, "Erica":erica}

# print(courseProgress)

'''👉 To access one item, I use two square brackets []. So to see only Erica's results, I would add:'''

# print(courseProgress["Erica"])

'''👉 What if we only want to see how many days Erica has completed?'''

# john = {"daysCompleted": 46, "streak": 22}
# janet = {"daysCompleted": 21, "streak": 21}
# erica = {"daysCompleted": 75, "streak": 6}

# courseProgress = {"John":john, "Janet":janet, "Erica":erica}

# print(courseProgress["Erica"]["daysCompleted"])



#___________________________

# print("Common Errors")
# print()
# print("Key Error")

'''👉 Why am I getting the 'key error'... error?'''

'''john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John":john, "Janet":janet, "Erica":erica}

print(courseProgress["Erica"]["daysComplete"])'''

# john = {"daysCompleted": 46, "streak": 22}
# janet = {"daysCompleted": 21, "streak": 21}
# erica = {"daysCompleted": 75, "streak": 6}

# courseProgress = {"John":john, "Janet":janet, "Erica":erica}

# print(courseProgress["Erica"]["daysCompleted"])

#___________________________

# print("Fix My Code")
# print()

'''
john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John":john, "Janet":janet, "Erica":erica}

print(courseProgress["erica"]["daysCompleted"])
print(courseProgress["Janet"]["Streak"])'''

# john = {"daysCompleted": 46, "streak": 22}
# janet = {"daysCompleted": 21, "streak": 21}
# erica = {"daysCompleted": 75, "streak": 6}

# courseProgress = {"John":john, "Janet":janet, "Erica":erica}

# print(courseProgress["Erica"]["daysCompleted"])
# print(courseProgress["Janet"]["streak"])

#___________________________

print("👉 Day 46 Challenge")
print()

print("🌟MokeBeast Generator🌟")
print()

import os, time

mokedex = {}

def prettyPrint():
  print(f"Name\tType\tHP\tMP")
  for key, value in mokedex.items():
    print(f"""{key:^12}|{value["type"]:^10}|{value["hp"]:^6}|{value["mp"]:^6}""")

while True:
  print("Add your Beast!")
  name = input("Name > ").title()
  type = input("Type > ").title()
  hp = int(input("HP > "))
  mp = int(input("MP > "))
  mokedex[name] = { "type": type, "hp": hp, "mp": mp}
  print("----------")
  print()
  prettyPrint()







#replit100DaysOfCode