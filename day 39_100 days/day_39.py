# Hangman
# Project Day! Flashback to your childhood and build your own version of Hangman.


# I built Hangman. Can you guess the word? Day 39 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python


# print("Hangman")
# print()
# import random
# listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

# wordChosen = random.choice(listOfWords)

# _________________________________________________________________________________________________________________


print("👉 Day 39 Challenge")
print()
print("🌟Hangman🌟")
import random, os, time

listOfWords = ["apple", "orange", "grapes", "pear"]
letterPicked = []
lives = 6

word = random.choice(listOfWords)

while True:

    letter = input("Choose a letter: ").lower()

    if letter in letterPicked:
        print("You've tried that before")
        continue

    letterPicked.append(letter)

    if letter in word:
        print("You found a letter")
    else:
        print("Nope, not in there")
        lives -= 1

    allLetters = True
    print()
    for i in word:
        if i in letterPicked:
            print(i, end="")
        else:
            print("_", end="")
            allLetters = False
    print()

    if allLetters:
        print(f"You won with {lives} left!")
        break

    if lives <= 0:
        print(f"You ran out of lives! The answer was {word}")
        break
    else:
        print(f"Only {lives} left")
time.sleep(3)
os.system("clear")


#replit100DaysOfCode