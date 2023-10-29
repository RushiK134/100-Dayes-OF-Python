# MokeBeast
# Gotta catch 'em all! Use dictionaries to create a game with small creatures you captured and forced to fight for your amusement. You monster.



# I caught 'em all with my epic MokeBeasts game. Day 42 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python



print("👉 Day 42 Challenge")
print()

print("👾 MokeBeast - The Non-Copyright Generic Beast Battle Game 👾")
print()
print()

# beastName = input("Input your beast's name: ").strip().capitalize()
# print()

# type = input("Input your beast's type: ").strip().title()
# print()

# specialMove = input("Input your beast's special move: ").strip().title()
# print()

# hp = input("Input your beast's staring HP: ").strip()
# print()

# mp = input("Input your beast's staring MP: ").strip()
# print()

# mokedex = {"Beast Name": beastName, "Type": type, "Special Move": specialMove, "HP": hp, "MP": mp}

# print()
# print()

# print("👾MokeBeast👾")
# print()

# if mokedex["Type"]=="Earth":
#   print("\033[32m", end="")
# elif mokedex["Type"]=="Air":
#   print("\033[37m", end="")
# elif mokedex["Type"]=="Fire":
#   print("\033[31m", end="")
# elif mokedex["Type"]=="Water":
#   print("\033[34m", end="")
# else:
#   print("\033[33m", end="")

# for name, value in mokedex.items():
#     print(f"{name:<15}:{value}")


#___________________________________________________________________or___________________________________


mokedex = {"Beast Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}


for name, values in mokedex.items():
  mokedex[name] = input(f"{name}:\t").strip().title()

if mokedex["Type"]=="Earth":
  print("\033[32m", end="")
elif mokedex["Type"]=="Air":
  print("\033[37m", end="")
elif mokedex["Type"]=="Fire":
  print("\033[31m", end="")
elif mokedex["Type"]=="Water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")

print("👾MokeBeast👾")
print()

for name, value in mokedex.items():
  print(f"{name:<15}: {value}")


#replit100DaysOfCode