# Video Game Characters
# Project Day! Build some characters and create their health and strength stats through the power of return, libraries, and loops. Get them ready to battle on Day 28.


# Getting ready for an epic battle tomorrow! But first, we need to build some characters 🧙🏻‍♀️🧝🏻‍♀️👺! Day 27 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python


import random, os, time

print("👉 Day 27 Challenge")
print()
time.sleep(1)
print("Character Builder")
print()
time.sleep(1)


def charName():
  userInputCharName = input("Name Your Legend: ")
  userInputCharType = input("Character Type (Human, Elf, Wiard, Orc): ")
  return userInputCharName, userInputCharType


def rollDice(slides):
  result = random.randint(1, slides)
  return result


def slideDice1():
  slide6 = rollDice(6)
  slide12 = rollDice(12)
  healthFormla = ((slide6 * slide12) / 2) + 10
  return healthFormla


def slideDice2():
  slide6 = rollDice(6)
  slide12 = rollDice(12)
  strengthFormula = ((slide6 * slide12) / 2) + 12
  return strengthFormula


# nextChar = "yes"
# while nextChar == "yes":
while True:
  print("⚔️Character generator⚔️")
  print()
  userInputCharName = input("Name Your Legend: ")
  userInputCharType = input("Character Type (Human, Elf, Wiard, Orc): ")
  time.sleep(1)
  os.system("clear")
  health = str(slideDice1())
  strength = str(slideDice2())
  print(userInputCharName,"has")
  print("HEALTH:", health, "hp")
  print("STRENGTH:", strength)
  print("May your name go down in Legend...")

  nextChar = input("Want to create another character?:- ")
  if nextChar == "No" or nextChar == "no":
    break

  time.sleep(1)
  os.system("clear")





#replit100DaysOfCode
#characterGenerator
