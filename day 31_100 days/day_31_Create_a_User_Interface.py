# Create a User Interface
# Project Day! Let creativity shine as you create two classic user interfaces using only `print` and `f-strings`.

# I went retro 🪩 and recreated two classic user interfaces. Can you guess what they are? Day 31 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python


print("👉 Day 31 Challenge")
print()
print("classic user interface using string manipulation")
print()
print()


def newPrint(color):
    if color == "red":
        return ("\033[31m")
    elif color == "yellow":
        return ("\033[33m")
    elif color == "blue":
        return ("\033[34m")
    elif color == "white":
        return ("\033[0m")
    elif color == "green":
        return ("\033[32m")
    elif color == "purple":
        return ("\033[35m")


title = f"{newPrint('red')}={newPrint('white')}={newPrint('blue')}={newPrint('yellow')} Music App {newPrint('blue')}={newPrint('white')}={newPrint('red')}="

print(f"       {title: ^35}")
print(f"🔥▶\t{newPrint('white')}Radio Gaga")
print(f"\t{newPrint('yellow')}Queen")

prev = "prev"
next = "next"
pause = "pause"

print(f"{newPrint('white')}{prev:<35}")
print(f"{newPrint('green')}{next:^35}")
print(f"{newPrint('purple')}{pause:>35}")

print()
print()
text = "WELCOME TO"
print(f"{newPrint('white')}{text:^35}")
text = "_ _    ARMBOOK    _ _"
print(f"{newPrint('blue')}{text:^35}")
print()
text = "Definitely not a rip off"
print(f"{newPrint('yellow')}{text:>35}")
text = "a certain other social"
print(f"{newPrint('yellow')}{text:>35}")
text = "networking site."
print(f"{newPrint('yellow')}{text:>35}")
print()
text = "Honest."
print(f"{newPrint('red')}{text:^35}")
print()
text = "Username: "
username = input(f"{newPrint('white')}{text:^35}")
text = "Password: "
username = input(f"{newPrint('white')}{text:^35}")





#replit100DaysOfCode