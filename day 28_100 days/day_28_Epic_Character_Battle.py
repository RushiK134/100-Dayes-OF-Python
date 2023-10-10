# Epic Character Battle
# Project Day! Your characters you built on Day 27 will fight to the death. Who will win out?

# Ready to battle it out ⚔️ with the characters I built in the previous day.  Day 28 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python


import random, os, time

print("👉 Day 28 Challenge")
print()
time.sleep(1)
print("Character Builder Part 2")
print()
time.sleep(1)


def rollDice(slides):
    result = random.randint(1, slides)
    return result


def health():
    healthFormla = ((rollDice(6) * rollDice(12)) / 2) + 10
    return healthFormla


def strength():
    strengthFormula = ((rollDice(6) * rollDice(12)) / 2) + 12
    return strengthFormula


print("⚔️Battle Time⚔️")
print()
c1Name = input("Name Your Legend:\n")
c1Type = input("Character Type (Human, Elf, Wiard, Orc):\n")
print()
c1Health = health()
c1strength = strength()
print(c1Name)
print("HEALTH:", c1Health, "hp")
print("STRENGTH:", c1strength)
print("")
print("Who are they battling?")
print()

c2Name = input("Name Your Legend:\n")
c2Type = input("Character Type (Human, Elf, Wiard, Orc):\n")
print()
c2Health = health()
c2strength = strength()
print(c2Name)
print("HEALTH:", c2Health, "hp")
print("STRENGTH:", c2strength)
print()

winner = None
round = 1
while True:
    time.sleep(1)
    os.system("clear")

    print("⚔️Battle Time⚔️")
    print()
    print("⚔️The battle begins!⚔️")

    c1Dice = rollDice(6)
    c2Dice = rollDice(6)

    difference = abs(c1strength - c2strength) + 1

    if c1Dice > c2Dice:
        c2Health -= difference
        if round == 1:
            print(c1Name, "wins the first blow")
        else:
            print(c1Name, "wins round", round)
    elif c2Dice > c1Dice:
        c1Health -= difference
        if round == 1:
            print(c2Name, "wins the first blow")
        else:
            print(c2Name, "wins round", round)
    else:
        print("Their swords clash and they draw round", round)

    print()
    print(c1Name)
    print("HEALTH:", c1Health, "hp")
    print()
    print(c2Name)
    print("HEALTH:", c2Health, "hp")
    print()

    if c1Health <= 0:
        print(c1Name, "has Died!")
        winner = c2Name
        break
    elif c2Health <= 0:
        print(c2Name, "has Died!")
        winner = c1Name
        break
    else:
        print("And they both standing for rhe next round")
        round += 1

time.sleep(1)
os.system("clear")

print("⚔️Battle Time⚔️")
print()
print(winner, "has won in", round, "rounds")

# replit100DaysOfCode
# characterGenerator
