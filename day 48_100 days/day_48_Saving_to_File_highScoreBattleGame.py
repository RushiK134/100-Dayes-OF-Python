# Saving to Files
# It only took 48 days (sorry about that), but we are finally going to save our data to 'files'.

# Finally know how to save my data. Day 48 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python





# print("File Writing")
# print()
# f= open(file name, Mode)
# file name can be any extension
# (mode are 'w' for write, 'a' for append, 'r' for read,and 'a+' for append and read)

# 'w' if file dosent exist it create it as a blank file and if the file already exist it will delete it and create a blank file

# f = open("savedFile.txt", "w")
# f.write("Hello there")
# f.close()
#_________________________________________

# print()
# print("Saving to Files")
# print()

# f = open("savedFile.txt", "w")
# whatText = input(">")
# f.write(whatText)
# f.close()
#it print it like this "So I Will"

# f = open("savedFile.txt", "a+")
# whatText = input(">")
# f.write(whatText)
# f.close()

# It print it like this "So I WillHere's some more"
# previous text and new text is connected to each other

#_________________________________________
# so for new line

# f = open("savedFile.txt", "a+")
# whatText = input(">")
# f.write(f"{whatText}\n")
# f.close()

#_________________________________________

# print()
# print("Common Errors")
# print()

# print("I/O operation error")

'''f = open("savedFile.txt", "a")
whatText = input("> ")
f.write(f"{whatText}\n")
f.close()
whatText = input("> ")
f.write(f"{whatText}\n")'''

# f = open("savedFile.txt", "a")
# whatText = input("> ")
# f.write(f"{whatText}\n")
# whatText = input("> ")
# f.write(f"{whatText}\n")
# f.close()

#_________________________________________

# print()
# print("Fix My Code")
# print()

'''f = open("savedFoal.", "a")
whatText = input("> ")
f.write(f"{whatText}\n")
f.close
whatText = input("> ")
f.write(f"{whatText}\n")'''

# f = open("savedFile.txt", "a+")
# whatText = input("> ")
# f.write(f"{whatText}\n")
# whatText = input("> ")
# f.write(f"{whatText}\n")
# f.close()

#_________________________________________

print()
print("👉 Day 48 Challenge")
print()

import os, time

while True:
  print("🌟HIGH SCORE TABLE🌟")
  print()
  name = input("Input your initials > ").upper()
  score = input("Input your score > ")
  print()

  f = open("high.score", "a+")
  f.write(f"{name} {score}\n")
  f.close()

  print("ADDED")
  time.sleep(1)
  os.system("clear")


#replit100DaysOfCode