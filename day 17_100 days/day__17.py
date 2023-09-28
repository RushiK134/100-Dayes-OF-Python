# Let's Cheat Continue
# Learn the `continue` command. An ideal component of building games AND build your first game that keeps score!

#New and improved 🪨 📄✂️ game! Day 17 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python

# while True:
#   print("You are in a coridoor, do you go left of right?")
#   direction = input(":- ")
#   if direction == "left":
#     print("You have fallen to your death")
#     break
#   elif direction == "right":
#     continue
#   else:
#     print("Ahh! You'r a genius, you've won")
#     exit()
# print("The game is over, you've filed!")


# __________________________________________________________________________________________________________________________________

# print("👉 What is wrong here?")
# print("Fix My Code")


'''while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit
print("The game is over, you've failed!")'''

# while True:
#   print("You are in a corridor, do you go left or right?")
#   direction = input("> ")
#   if direction == "left":
#     print("You have fallen to your death")
#     break
#   elif direction == "right":
#     continue
#   else:
#     print("Ahh! You're a genius, you've won")
#     exit()
# print("The game is over, you've failed!")

# _____________________________________________

'''print("Let's play chutes and ladders. Pick ladder or chute.")
while True:
  print("Do you want to go up the ladder or down the chute?")
  direction = input("> ")
  if direction == "chute"
    print("Game over!")
  break
  elif direction == "ladder":
    continue
else:
    print("Game over!")
    exit 
print("Thanks for playing!")'''

# print("Let's play chutes and ladders. Pick ladder or chute.")
# while True:
#   print("Do you want to go up the ladder or down the chute?")
#   direction = input("> ")
#   if direction == "chute":
#     print("Game over!")
#     break
#   elif direction == "ladder":
#     continue
#   else:
#     print("Game over!")
#     exit()
# print("Thanks for playing!")

print("Day 17 Challange")

from getpass import getpass as input

print("2 player 🪨📄✂️")

print(" ")

print("E P I C    🪨  📄 ✂️    B A T T L E ")

print(" ")

print("select your move( R, P or S)")

print(" ")
print("Input is not visible because each player cannot see what the other player typed in 😉.")
print("So please use Caps Lock to play the game")
print(" ")
count1 = 0
count2 = 0
while True:
    player1 = input("Player 1: ")
    print("")
    player2 = input("Player 2: ")
    print("")

    if player1 == "R":
        if player2 == "R":
            print("You both oucked Rock 🪨x🪨,draw!")
        elif player2 == "S":
            print("Player1 smashed Player2's Scissors with their Rock! 🪨x✂️")
            count1 += 1
        elif player2 == "P":
            print("Player1's Rock is smothered by Player2's Paper! 🪨x📄")
            count2 += 1

    elif player1 == "P":
        if player2 == "R":
            print("Player2's Rock is smothered by Player1's Paper! 📄x🪨")
            count1 += 1
        elif player2 == "S":
            print("Player1's Paper is cut by Player2's Scissors! 📄x✂️")
            count2 += 1
        elif player2 == "P":
            print("You both oucked Paper 📄x📄,draw!")

    elif player1 == "S":
        if player2 == "R":
            print("Player2 smashed Player1's Scissors with their Rock! ✂️x🪨")
            count2 += 1
        elif player2 == "S":
            print("You both oucked Scissor ✂️x✂️,draw!")
        elif player2 == "P":
            print("Player2's Paper is cut by Player1's Scissors! ✂️x📄")
            count1 += 1

    print("Player 1 has", count1, "wins.")
    print("Player 2 has", count2, "wins.")

    if count1 == 3 or count2 == 3:
        print("Thanks for playing!")
        exit()

    else:
        continue


#replit100DaysOfCode