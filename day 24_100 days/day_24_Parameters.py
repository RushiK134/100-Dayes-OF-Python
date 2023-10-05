# Roll in the Parameters
# Underwhelmed by subroutines? Let's switch it up and add some parameters.

# They see me rollin' ( 🎲 ), they hatin'.  Day 24 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python


# print("Parameters in Subroutines")

# print("")

# def whichCake(ingredient):
#   if ingredient == "chocolate":
#     print("Mmm,chocoolate cake is amazing")
#   elif ingredient == "broccoli":
#     print("you what mate?!")
#   else:
#     print("Yeah, that's grate I suppose.... ")

# whichCake("broccoli")

# ______________________________________________________________________________________________________

# print("")

# print("Adding More Arguments")

# print("")

# def whichCake(ingredient, base, coating):
#   if ingredient == "chocolate":
#     print("Mmm,chocoolate cake is amazing")
#   elif ingredient == "broccoli":
#     print("you what mate?!")
#   else:
#     print("Yeah, that's grate I suppose.... ")
#   print("So you want a", ingredient,"cake on a",base,"base with",coating,"on top?")

# userIngredien = input("Name the Ingredient: ")
# userBase = input("Name a type of Base: ")
# userCoating = input("Fave cake Topping: ")

# whichCake(userIngredien, userBase, userCoating)

# __________________________________________________________________________________

# print("")

# print("Common Errors")

# print("")

'''def biggerNumber(number1 number2):
  if(number1 > number2):
    print(number 1, "is bigger")
  else:
    print(number 2, "is bigger")

biggerNumber (18,332)'''

# def biggerNumber(number1, number2):
#   if(number1 > number2):
#     print(number1,"is bigger")
#   else:
#     print(number2, "is bigger")

# biggerNumber (18,332)

# ___________________________________________________________________________________________________


# print("")

# print("Fix My Code")

# print("")

'''def pizza_order(topping1 topping2):
  if topping1 = "pepperoni":
    print(topping1, "is a great choice")
  else:
    print(topping1, "is kinda lame on pizza")
  print(topping2, "sounds delicious, much better than" topping1)

topping1 =  input("Name a pizza topping. ")
topping2 = input("Name a second pizza topping. ")

  pizza_order(topping1, topping2)'''

# def pizza_order(topping1,topping2):
#   if topping1 == "pepperoni":
#     print(topping1, "is a great choice")
#   else:
#     print(topping1, "is kinda lame on pizza")
#   print(topping2, "sounds delicious, much better than", topping1)

# topping1 =  input("Name a pizza topping. ")
# topping2 = input("Name a second pizza topping. ")

# pizza_order(topping1, topping2)

# __________________________________________________________________________________________________

# print("")

print("👉 Day 24 Challenge")

print("")

print("Infinity Dice 🎲")

print("")

import random

sides = int(input("how many sides the dice should be?:- "))
playGame = "yes"


def rollDice(sides):
    print("You rolled ", random.randint(1, sides))


while playGame == "yes":
    rollDice(sides)
    playGame = input("Roll aganin?:- ")

#replit100DaysOfCode