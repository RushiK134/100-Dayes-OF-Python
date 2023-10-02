# Use other people's code
# Let's be sneaky and learn how to use other people's code to make your life easier.

# Guess the number between one and 1Million!! Closest guess gets a shout-out from Replit team @LessonHacker and @AarrrMe! Day 22 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python

print("Libraries")
print()
print("Random library")

# import random

# myNumber = random.randint(1,100)
# print(myNumber)

#_________________________________________________________________

# print("Common Errors")
# print()

'''import random

myNumber = randint(1, 100)
print(myNumber)'''

# import random

# myNumber = random.randint(1, 100)
# print(myNumber)

#_________________________________________________________________

# print()
# print("Error with random numbers and loops")
# print()

'''import random

myNumber = random.randint(1, 100)
for i in range(10):
  print(myNumber)'''

# import random
# for i in range(10):
#   myNumber = random.randint(1, 100)
#   print(myNumber)

#_________________________________________________________________

# print()
# print("Error with random numbers and loops")
# print()

'''importrandom

myNumber = .randint(1, 10)
for i in range(10):
  print(myNumber)'''

# import random

# for i in range(10):
#   myNumber = random.randint(1, 10)
#   print(myNumber)


#_________________________________________________________________

print()
print("Day 22 Challenge")
print()

print("Welcome to Guess the Number.")

print("")

print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")

print("")
import random
correctNumber = random.randint(1, 1000000)
count = 0

while True:
  pickNumber = int(input("What is your guess?: "))

  if pickNumber < 0:
    print("We'll never know what the answer is …")
    break
  if pickNumber < correctNumber:
    print("That number is too low. Try again!")
    count += 1
  elif pickNumber > correctNumber :
    print("That number is too high. Try again!")
    count += 1
    continue
  elif pickNumber == correctNumber:
    print("You are a winner! 🥳🥳")
    break
  else:
    print("That is not a number I recognize.")

print("It took you", count, "attempt(s) to get the correct answer.")


#replit100DaysOfCode