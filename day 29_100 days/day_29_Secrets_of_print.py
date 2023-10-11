# The Secrets of print
# You already learned how to `print` like a boss, but there are a few things you can do make them even easier.

# Bringing `print` statements to life with COLOR! Day 29 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python

# print("second arguments to the print statement")
# print()

# print("Secret One: end")
# print()
# print("Add a space")
# print()
# for i in range(0, 100):
#   print(i, end=" ")

# print()
# print("Add a space and comma")
# for i in range(1,100):
#   print(i,end = ", ")

# print()
# print("Add a new line, tab, or vertical tab")
# print()
# #new line
# for i in range(0, 100):
#   print(i, end="\n")

# print()

# #new line
# for i in range(0, 100):
#   print(i, end="\t")

# print()
# #vertical tab
# for i in range(0, 100):
#   print(i, end="\v")

# print()

# print()
# print("Add a space")
# print()

#___________________________________________________________________________________________________

# print("Secret Two: sep")
# print()
# print("Color Changing with end...")

# print()
# print("If you put")
# print("\033[33m",end="") #yellow
# print("nothing as the")
# print("\033[35m", end="") #purple
# print("end character")
# print("\033[32m", end="") #green
# print("then you don't")
# print("\033[0m", end="") #default
# print("get odd gaps")

# print()
# print("If you put", "\033[33m", "nothing as the", "\033[35m", "end character", "\033[32m", "then you don't", "\033[0m", "get odd gaps", end="")

# print()
# print("Color Changing with sep...")
# print()
# print("If you put ", "\033[33m", "nothing as the ", "\033[35m", "end character ", "\033[32m", "then you don't ", "\033[0m", "get odd gaps ", sep="")

#_______________________________________________________________________________________________

# print("Secret Three: Cursor")
# print()
# print("👉 Do you notice how difficult this is to read?")

# print()

# import os
# for i in range(1,100):
#   print(i)
#   os.system("clear")

# print()
# print("Your probably thinking...Rushi, import time:")
# print()
# print("👉 Let's do it, but is there anything you still notice?")
#
import os, time
# import os,time
# for i in range (1,100):
#   print(i)
#   time.sleep(0.5)
#

# print()
# print("That GIANT white cursor...")
# print()
'''👉 Let's try the same code, but turn the cursor off: print('\033[?25l', end="")   '''

# import os, time
# print('\033[?25l', end="")
# for i in range(1, 101):
#   print(i)
#   time.sleep(0.1)
#   os.system("clear")
'''What if we want to turn the cursor back on:print('\033[?25h', end="")'''
# print('\033[?25h', end="")


#_________________________________________________________________________________________________

print("👉 Day 29 Challenge")
'''
 """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
    '''
print()
def newPrint(color, word):
  if color=="red":
    print("\033[31m", word, sep="", end="")
  elif color=="green":
    print("\033[32m", word, sep="", end="")
  elif color=="blue":
    print("\033[34m", word, sep="", end="")
  elif color=="normal":
    print("\033[0m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")

print("Super Subroutine")
print("With my ", end="")
newPrint("red", "new program")
newPrint("reset", " I can just call red('and') ")
newPrint("red", "it will print in red ")
newPrint("blue", "or even blue")



#replit100DaysOfCode