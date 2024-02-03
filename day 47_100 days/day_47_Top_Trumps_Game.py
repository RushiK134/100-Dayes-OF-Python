# Top Trumps
# Not heard of 'Top Trumps'? Maybe because it's British...and so is David. Anyways, use 2D dictionary skills for this card game battle.

# Channelled my inner British 🇬🇧 vibes and recreated David's favorite card game. Day 47 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python


print("👉 Day 47 Challenge")
print()
print("🌟Top Trumps🌟")
print()

import os, time, random

trumps = {}
trumps["David"] = {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness Level": 99}
trumps["Mr Spock"] = {"Intelligence": 200, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Moica from Friends"] = {"Intelligence": 150, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Professor X"] = {"Intelligence": 250, "Speed": 1, "Guile": 200, "Baldness Level": 101}

while True:
    print("TOP TRUMPS")
    print()
    print("Characters")
    print()
    for key in trumps:
        print(key)
    user = input("Pick your character\n> ")
    comp = random.choice(list(trumps.keys()))
    print("Computer has picked", comp)

    print("Choos your stat: Intelligence, Speed, Guile & Baldness Level")

    answer = input("> ")

    print(f"{user}: {trumps[user][answer]}")
    print(f"{comp}: {trumps[comp][answer]}")

    if trumps[user][answer] > trumps[comp][answer]:
        print(user, "wins")
    elif trumps[user][answer] < trumps[comp][answer]:
        print(comp, "wins")
    else:
        print("Draw")

    time.sleep(2)
    os.system("clear")

#replit100DaysOfCode