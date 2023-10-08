# The Power of Libraries in Games
# You are 1/4th of the way done with 100 Days of Code! Well done. Learn how to import two libraries: 'os' and 'time', which will be super helpful as you start to build some really cool automation.


# Used @Replit's cool audio feature to build an iPod and listen to some tunes 🎵. Day 26 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python

# print("os Library")

# import os

# print("")

# for i in range(1,1000):
#   print(i)
#   os.system("clear")

# print("")
#__________________________________________________________________________
# print("Time Library")

# import os,time
# print("Welcome")
# print("to")
# print("Replit")

# time.sleep(1)
# os.system("clear")

# username = input("Username: ")

# print("")
#__________________________________________________________________________

print("👉 Day 26 Challenge")

print("")

from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False
  while True:
    stopPlay = int(input("Press 2 anytime to stop payback and go back to the menu: "))
    if stopPlay == 2:
      source.paused = True
      return
    else:
      continue

while True:
  # clear the screen
  os.system("clear")
  # Show the menu
  print("🎵 MyPOD Music Player")
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit")
  time.sleep(1)
  print("Press anything else to see the menu again.")
  # take user's input
  userInput = int(input("> "))
  if userInput == 1:
    print("Playing some proper tunes!")
    play()
  elif userInput == 2:
    exit()
  else:
    continue









#replit100DaysOfCode
