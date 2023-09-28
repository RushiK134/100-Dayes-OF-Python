# Guess the Numbe
# Build a 'Guess the Number' game where the user has to read your mind and guess the number you are thinking...

# Can you "Guess the Number" I have in mind 🤔? Day 18 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python


print("👉 Day 18 Challenge")

print("")

print("Welcome to Guess the Number.")

print("")

print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")

print("")

correctNumber = 2100
count = 0

while True:
  pickNumber = int(input("What is your guess?: "))

  if pickNumber < 0:
    print("We'll never know what the answer is …")
    break
  if pickNumber < correctNumber:
    print("That number is too low. Try again!")
    count += 1
  elif pickNumber > correctNumber :
    print("That number is too high. Try again!")
    count += 1
    continue
  elif pickNumber == correctNumber:
    print("You are a winner! 🥳🥳")
    break
  else:
    print("That is not a number I recognize.")

print("It took you", count, "attempt(s) to get the correct answer.")


#replit100DaysOfCode