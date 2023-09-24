# Rock, Paper, Scissors
# Day 14! Now for the most epic of projects...a rock, paper, scissors game to share with the community.


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

player1 = input("Player 1: ")
print("")
player2 = input("Player 2: ")
print("")

if player1 == "R":
    if player2 == "R":
        print("You both oucked Rock 🪨x🪨,draw!")
    elif player2 == "S":
        print("Player1 smashed Player2's Scissors with their Rock! 🪨x✂️")
    elif player2 == "P":
        print("Player1's Rock is smothered by Player2's Paper! 🪨x📄")
    else:
        print("Invalid Move Player 2!")

elif player1 == "P":
    if player2 == "R":
        print("Player2's Rock is smothered by Player1's Paper! 📄x🪨")
    elif player2 == "S":
        print("Player1's Paper is cut by Player2's Scissors! 📄x✂️")
    elif player2 == "P":
        print("You both oucked Paper 📄x📄,draw!")
    else:
        print("Invalid Move Player 2!")

elif player1 == "S":
    if player2 == "R":
        print("Player2 smashed Player1's Scissors with their Rock! ✂️x🪨")
    elif player2 == "S":
        print("You both oucked Scissor ✂️x✂️,draw!")
    elif player2 == "P":
        print("Player2's Paper is cut by Player1's Scissors! ✂️x📄")
    else:
        print("Invalid Move Player 2!")

else:
    print("Invalid Move Player 1!")


# replit100DaysOfCode
