# Subroutines: The Recipe for Coding
# Write code in a way where you can use it, call it, or repeat it anywhere and at anytime with the power of subroutines.

# Ok you might have cracked my earlier login but let's try a better one 🔐 ! Day 23 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python


print("Subroutine")

'''So far, when we wanted to repeat code, we have had to use loops or copy and paste code.

What if I told you there was a way to use code or call it and use it anytime anywhere??

That is a subroutine!!

A subroutine tells the computer that a piece of code exists and to go run that code again and again...
Just like a recipe

Subroutines work like a recipe in a cookbook. If you want to know how to make a cake, you don't have to start from scratch every time. You can use a recipe to get the same quality each time.'''

# print("")

# def rollDice():
#   import random
#   dice = random.randint(1, 6)
#   print("you rolled: ",dice)

# for i in range(10):
#   rollDice()
# ___________________________________________________________________


print("")

# print("Common Errors")

'''def print My Name():
  print("My Name is David")

print My Name()'''

# def printMyName():
#   print("My Name is David")

# printMyName()
# ___________________________________

'''def countToFive:
  for i in range(1, 6):
    print(i)

countToFive()'''

# def countToFive():
#   for i in range(1, 6):
#     print(i)

# countToFive()

# ______________________________________
print("")

'''def countToFive():
  for i in range(1, 6):
    print(i)

  countToFive()'''

# def countToFive():
#   for i in range(1, 6):
#     print(i)

# countToFive()

# _________________________________________________________________________

# print("Fix My Code")

# print("")

'''def print favorite color:
  print("My favorite color is red.)

  print favorite color()'''

# def printFavoriteColor():
#   print("My favorite color is red.")

# printFavoriteColor()

# ________________________________

# def countToFive():
#   for i in range(1,6):
#     print(i)

# countToFive()


# ___________________________________________________________________________________________


print("👉 Day 23 Challenge")

print("")


def replitLoginSystem():
    while True:
        userName = input("Enter User Name:- ")
        inputPass = input("Enter Pass Word:- ")
        if userName == "david" and inputPass == "valdies4life":
            print("Welcome David!")
            break

        else:
            print("Whoops! I don't recognize that username or password. Try again!")
            continue


print("Welcome to Replit!")
replitLoginSystem()

#replit100DaysOfCode
