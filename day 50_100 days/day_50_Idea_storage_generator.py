# Idea Storage
# Do you have brilliant ideas at inconvenient times? Need a handy way to store them? Then, today's project is for you!

# I will never forget a brilliant idea again thanks to my idea storage system. Halfway there with Day 50 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python

print("👉 Day 50 Challenge")
print()
print("🌟Idea Storage🌟")
print()
import random, os, time
def add():
  os.system("clear")
  idea = input("Idea >> ")
  f = open("my.ideas", "a+")
  f.write(f"{idea}\n")
  f.close()
  print("Added")
  time.sleep(1)
  os.system("clear")

def show():
  os.system("clear")
  f = open("my.ideas", "r")
  ideas = f.read().split("\n")
  f.close()
  ideas.remove("")
  idea = random.choice(ideas)
  print(idea)
  time.sleep(2)
  os.system("clear")

while True:
  print("🌟Idea Storage🌟")
  print()
  menu = input("1: Add an idea\n2: Load up a random idea\n>> ")

  if menu == "1":
    add()
  else:
    show()

#replit100DaysOfCode