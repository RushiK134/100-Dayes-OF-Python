# Send it Back
# The `return` command will allow you to really start building some epic, automated video games.

# Built a character health stats generator to prepare for the epic battle in 3 days!! Day 25  of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python


print("Return Command")

print("")

# print("random pin Number Generator")

# print("")

# #subroutine has parameter called `number`
# #`number` shows how many numbers we want the pin to have

# def pinPicker(number):
#   import random
#   pin = " "   #empty string
#   for i in range(number): #for loop shows defined amount of random numbers
#     pin += str(random.randint(0,9))  #we want a string of random numbers between 0-9
#   return pin
# myPin = pinPicker(4)  #4 means we want 4 random numbers
# print(myPin)

# print("")
# __________________________________________________________________________

# print("Common Errors")

# print("")

'''def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area

areaOfTriangle (5, 22)
print(area)'''

# print("area of triangle")
# def areaOfTriangle(base, height):
#   area = 0.5 * base * height
#   return area

# area = areaOfTriangle (5, 22)
# print(area)

# ________________________________________________-

# print("")

# print("Fix My Code")

# print("")
# print("Area of Square")
# print("")

'''def area_square(side1 side2):
  area = side1 * side2
  return area_square

area_square(4, 12)
print(area)'''

# def area_square(side1, side2):
#   area = side1 * side2
#   return area

# area = area_square(4, 12)
# print(area)

# __________________________________________________________________

print("👉 Day 25 Challenge")

print("")

# print("⚔️ Character Stats Generator ⚔️")

# print("")

# import random
# def rollDice(number):


#   return number


# nextChar = "yes"
# slide6 = random.randint(1, 6)
# slide8 = random.randint(1, 8)
# def slideDice(slide6,slide8):
#   # slide6 = random.randint(1, 6)
#   # slide8 = random.randint(1, 8)
#   multiply = slide6 * slide8
#   return multiply

# health = slideDice(slide6,slide8)

# while nextChar ==  "yes":
#   charName = input("Name your warrior: ")
#   print("Their health is ",health,"hp")
#   nextchar = input("Next Charactor?:- ")


import random


def rollDice(sides):
    result = random.randint(1, sides)
    return result


def slideDice():
    slide6 = rollDice(6)
    slide8 = rollDice(8)
    multiply = slide6 * slide8
    return multiply


print("⚔️Character stats generator⚔️")

nextChar = "yes"

while nextChar == "yes":
    charName = input("Name your warrior: ")
    multiply = str(slideDice())
    print("Their health is ", multiply, "hp")
    nextChar = input("Want to create another character?:- ")





#replit100DaysOfCode