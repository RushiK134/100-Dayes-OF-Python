# Reading a File
# Once we've got data into a file, wouldn't it be just splendid to load it back into our program to use again? Let's do it!


# write a content in file using this

# f = open("filename.list","a+")
# whattowrite = input("What do you want to write to the file? >> ")
# f.write(f"{whattowrite}\n")
# f.close()

# _________________________________________________________________

# Read and Close a file

# f = open("filename.list","r")
# contents = f.read()
# f.close()

# contents = contents.split()
# #added split here

# print(contents)

# _________________________________________________________________

# print("Read One Line At A Time(Single Line)")
# print()

# f = open("filename.list","r")

# contents = f.readline()
# print(contents)

# f.close()

# _________________________________________________________________

# print("Read One Line At A Time (Repeat)")
# print()

# f = open("filename.list","r")

# contents = f.readline().strip()
# print(contents)
# contents = f.readline().strip()
# print(contents)
# contents = f.readline().strip()
# print(contents)
# contents = f.readline().strip()
# print(contents)

# f.close()


# _________________________________________________________________

# print("To Read all Lines At A Time (for Repeat Just Use a Loop)")
# print()

# f = open("filename.list","r")
# while True:
#   contents = f.readline().strip()

#   if contents == "":
#     break
#   print(contents)
# f.close()

# _________________________________________________________________

# print("Common Errors")
# print()
# print("It's outputting a blank at the end?")
# print()

'''f = open("filenames.list","r")
while True:
  contents = f.readline().strip()
  print(contents)

  if contents == "":
    break'''

# f = open("filename.list","r")
# while True:
#   contents = f.readline().strip()

#   if contents == "":
#     break

#   print(contents)


# print("Make it stop! MAKE IT STOP!")
# print()

'''f = open("filenames.list","r")
while True:
  contents = f.readline().strip()

  print(contents)'''

# f = open("filename.list","r")
# while True:
#   contents = f.readline().strip()

#   if contents == "":
#     break

#   print(contents)


# _________________________________________________________________

# print("Fix My Code")
# print()

'''while True:
  contents = f.readline().strip()

  print(contents)'''

# f = open("filename.list","r")
# while True:
#   contents = f.readline().strip()

#   if contents == "":
#     break
#   print(contents)
# f.close()

# _________________________________________________________________

print("👉 Day 49 Challenge")
print()
print("🌟Current Leader🌟")
print()

import os, time

f = open("high.score", "r")
scores = f.read().split("\n")
f.close()

highscore = 0
name = None

for rows in scores:
    data = rows.split()
    if data != []:
        if int(data[1]) > highscore:
            highscore = int(data[1])
            name = data[0]

print("The winner is", name, "with", highscore)



#replit100DaysOfCode