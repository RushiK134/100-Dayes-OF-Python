# Dynamic 2D Lists
# What about 2D lists that change? Let's make David's Nan's Bingo game a bit more dynamic.


# Now, #DavidsNanIsGoingToWinAtBingo with the changes I made to the Bingo game. #DavidsNanLovesThisCode Day 44 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python


# print("2D Dynamic Lists")
# print()

# print("Loops, append() and break")
# print()

# listOfShame = []

# while True :
#   name = input("What is your name? : ")
#   age = input("What is your age? ")
#   pref = input("What is your computer platform? ")
#   row = [name, age, pref]
#   listOfShame.append(row)
#   exit = input("Exit? y/n")
#   if (exit.strip().lower()[0] == "y"):
#     break

#   print(listOfShame)


# ________________________________

# print("Pretty Printing")
# print()

# listOfShame = []

# def prettyPrint():
#   print()
#   for row in listOfShame:
#     print(row)
#   print()

# while True :
#   name = input("What is your name? : ")
#   age = input("What is your age? ")
#   pref = input("What is your computer platform? ")
#   row = [name, age, pref]
#   listOfShame.append(row)
#   exit = input("Exit? y/n")
#   if (exit.strip().lower()[0] == "y"):
#     break

#   print(listOfShame)

# _________________

# print("Prettier Printing?")
# print()


# listOfShame = []

# def prettyPrint():
#   print()
#   for row in listOfShame:
#     for item in row:
#       print(f"{item:^10}", end=" \ ")
#     print()
#   print()

# while True :
#   name = input("What is your name? : ")
#   age = input("What is your age? ")
#   pref = input("What is your computer platform? ")
#   row = [name, age, pref]
#   listOfShame.append(row)
#   exit = input("Exit? y/n")
#   if (exit.strip().lower()[0] == "y"):
#     break

#   print(listOfShame)

# ________________________________
# print("Common error")
# print()
# print("Add or Remove?")
# print()

# listOfShame = []

# def prettyPrint():
#   print()
#   for row in listOfShame:
#     for item in row:
#       print(f"{item:^10}", end=" \ ")
#     print()
#   print()

# while True :
#   menu = input("Add or Remove?")
#   if(menu.strip().lower()[0]=="a"):
#     name = input("What is your name? : ")
#     age = input("What is your age? ")
#     pref = input("What is your computer platform? ")
#     row = [name, age, pref]
#     listOfShame.append(row)
#   else:
#     name = input("What is the name of the record to delete?")
#     for row in listOfShame:
#       if name in row:
#         listOfShame.remove(row)

#   print(listOfShame)


# ________________________________

# print("Fix My Code")
# print()

# '''My Remove Doesn't Work And There's No Error?'''

'''
listOfShame = []

while True:
  menu = input("Add or Remove?")

  if(menu.strip().lower()[0]=="a"):

    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")

    row = [name, age, pref]

    listOfShame.append(row)


  else:
    name = input("What is the name of the record to delete?")

    if name in listOfShame:
      listOfShame.remove(name) # remove the whole row if name is in it


  print(listOfShame)'''

# listOfShame = []

# while True:
#   menu = input("Add or Remove?")

#   if(menu.strip().lower()[0]=="a"):

#     name = input("What is your name? ")
#     age = input("What is your age? ")
#     pref = input("What is your computer platform? ")

#     row = [name, age, pref]

#     listOfShame.append(row)


#   else:
#     name = input("What is the name of the record to delete?")
#     for row in listOfShame:
#       if name in row:
#         listOfShame.remove(row)

#   print(listOfShame)


# ________________________________

print("👉 Day 44 Challenge")
print()

import random, os, time

bingo = []


def ran():
    number = random.randint(1, 90)
    return number


def prettyPrint():
    for row in bingo:
        for item in row:
            print(item, end="\t|\t")
        print()


def createCard():
    global bingo
    numbers = []
    for i in range(8):
        num = ran()
        while num in numbers:
            num = ran()
        numbers.append(ran())

    numbers.sort()

    bingo = [[numbers[0], numbers[1], numbers[2]],
             [numbers[3], "BG", numbers[4]],
             [numbers[5], numbers[6], numbers[7]]
             ]


createCard()
while True:
    prettyPrint()
    num = int(input("Next Number: "))
    for row in range(3):
        for item in range(3):
            if bingo[row][item] == num:
                bingo[row][item] = "X"

    exes = 0
    for row in bingo:
        for item in row:
            if item == "X":
                exes += 1

    if exes == 8:
        print("You have won")
        break

    time.sleep(1)
    os.system("clear")

#replit100DaysOfCode