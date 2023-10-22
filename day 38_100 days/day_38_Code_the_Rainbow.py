# Code the Rainbow
# Code the rainbow by harnessing the power of string and loops.


# Code the rainbow and harness the power of strings and loops. Day 38 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python



# print("Strings and Loops")
# print()

# myString = "Day 38"
# for letter in myString:
#   print(letter)

#_________________________________________________________________

# print("if statement inside the loop")
# print()

# myString = "Day 38"
# for letter in myString:
#   if letter.lower() == "a":
#     print('\033[33m', end='') #yellow
#   print(letter)
#   print('\033[0m', end='') #back to default

#_________________________________________________________________


# print("Using a list to specify search items")
# print()

# vowels = ["a","e","i","o","u"]

# myString = "Will my vowels now be yellow?"
# for letter in myString:

#   if letter.lower() in vowels:
#     print('\033[33m', end='') #yellow

#   print(letter, end="")
#   print('\033[0m', end='') #back to default
#This is a comment. It is only for you. The computer will ignore it.


#_________________________________________________________________

print("👉 Day 38 Challenge")
print()

def colorChange(color):
  if color=="r":
    print("\033[31m", end="")
  elif color==" ":
    print("\033[0m", end="")
  elif color=="b":
    print("\033[34m", end="")
  elif color=="y":
    print("\033[33m", end="")
  elif color == "g":
    print("\033[32m", end="")
  elif color == "p":
    print("\033[35m", end="")

sentence = input("What sentence do you want rainbow-izing?: ")
for letter in sentence:
  colorChange(letter.lower())
  print(letter, end="")
print()





#replit100DaysOfCode