print("=== Ypur Advanture Simulator ==")
print("""You'll be asked a bunch of questions then we'll make you up an amazing story with YOU as the star! 🤩🤩...""")
print("")

name = input("Your name: ")
enemy = input("your woest enimy's name: ")
superPower = input("Enter super power: ")

print(" ")

# print("Once upon a time, in a world filled with magic and mystery, there was a hero named", name,".", name, "possessed an incredible superpower: ",superPower,". But lurking in the shadows was ",enemy, "the arch-nemesis of ",name,". The two were destined for a final showdown that would determine the fate of the entire world.")

print("Our story begins as our hero",name,"approaches a foreboding castle...")
print("Suddenly a bolt of lightning striked the ground and the feet of",name)
print("'Our final battle begins!' shouts the evil",enemy,"clearly missing the fact that",name,"has the power of",superPower,"whihch means they'll win quite easily")


# print("\033[text color code m")  command code thet tells the computer to change the text of colour to a different coolour
"""colour    value
    Default  0
    Black    30
    Red      31
    Green    32
    Yellow   33
    Blue     34
    Purple   35
    Cyan     36
    white    37 """

# Turn on Red text colour print("\033[31m"),then Turn of ot print("\033[0m") by Default
# use only \033[31m code inside print statement without spacing
print("")
print("")
print("")
print("")

print("Print in colors")

print("Our story begins as our hero",name,"approaches a foreboding castle...")
print("Suddenly a bolt of lightning striked the ground and the feet of",name)
print("\033[31m'Our final battle begins!'\033[0mshouts the evil",enemy,"clearly missing the fact that",name,"has the power of\033[35m",superPower,"\033[0mwhihch means they'll win quite easily")

#replit100DaysOfCode