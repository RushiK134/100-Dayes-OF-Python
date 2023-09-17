# Nesting Dolls Code
# Like nesting dolls, nest 'if' statements within 'if' statements. Create a game to find true fans of your favorite show.

# Nesting
# Nesting is where we put an if statement within an if statement using the power of indenting. The second if statement within the first if statement must be indented and its print statement needs to be indented one more time.


# tvShow = input("What is your favourite tv show?: ")
# if tvShow == "peppa pig":
#   print("Ugh, why?")
#   faveCharactor = input("who is your favourite character?: ")
#   if faveCharactor == "daddy pig":
#     print("Right answer")
#   else:
#     print("Nah, Daddy pig's the greatest")
# elif tvShow == "paw petrol":
#   print("Aww, sad times")
# else:
#   print("Yeah, that's cool and all...")

# print("")
# print("")
# _____________________________________________________
# print("🕵️‍♂️Fake Fan Finder👀")
# # Ask the user for their favorite anime
# favorite_anime = input("What's your favorite anime? ")

# # Check the favorite anime and ask questions accordingly
# if favorite_anime == "naruto":
#     # Ask questions about Naruto
#     print("Great choice! Let's talk about Naruto.")
#     question1 = input("Who is the main protagonist in Naruto? ")
#     if question1 == "naruto uzumaki":
#         print("That's correct! Naruto Uzumaki is the main protagonist.")
#     else:
#         print("Oops, that's not correct. It's Naruto Uzumaki.")

#     question2 = input("What is the name of Naruto's sensei? ")
#     if question2 == "kakashi hatake":
#         print("Correct! Kakashi Hatake is Naruto's sensei.")
#     else:
#         print("Nope, it's Kakashi Hatake.")

# elif favorite_anime == "one piece":
#     # Ask questions about One Piece
#     print("One Piece is a fantastic choice! Let's talk about it.")
#     question1 = input("Who is the captain of the Straw Hat Pirates? ")
#     if question1 == "monkey d. luffy":
#         print("That's right! Monkey D. Luffy is the captain.")
#     else:
#         print("Incorrect. It's Monkey D. Luffy.")

#     question2 = input("What is the ultimate goal of the Straw Hat Pirates? ")
#     if question2 == "find the One Piece":
#         print("Correct! Their goal is to find the One Piece treasure.")
#     else:
#         print("Wrong, it's to find the One Piece treasure.")

# else:
#     # For any other anime
#     print("I see you like", favorite_anime + ".")
#     print("Sorry, I don't have specific questions for that anime.")

# # End of the program
# print("Thanks for sharing your favorite anime with us!")
# -----------------------------------------------------
# # lower casing input
# print("🕵️‍♂️Fake Fan Finder👀")
# # Ask the user for their favorite anime
# favorite_anime = input("What's your favorite anime? ")

# # Check the favorite anime and ask questions accordingly
# if favorite_anime.lower() == "naruto":
#     # Ask questions about Naruto
#     print("Great choice! Let's talk about Naruto.")
#     question1 = input("Who is the main protagonist in Naruto? ")
#     if question1.lower() == "naruto uzumaki":
#         print("That's correct! Naruto Uzumaki is the main protagonist.")
#     else:
#         print("Oops, that's not correct. It's Naruto Uzumaki.")

#     question2 = input("What is the name of Naruto's sensei? ")
#     if question2.lower() == "kakashi hatake":
#         print("Correct! Kakashi Hatake is Naruto's sensei.")
#     else:
#         print("Nope, it's Kakashi Hatake.")

# elif favorite_anime.lower() == "one piece":
#     # Ask questions about One Piece
#     print("One Piece is a fantastic choice! Let's talk about it.")
#     question1 = input("Who is the captain of the Straw Hat Pirates? ")
#     if question1.lower() == "monkey d. luffy":
#         print("That's right! Monkey D. Luffy is the captain.")
#     else:
#         print("Incorrect. It's Monkey D. Luffy.")

#     question2 = input("What is the ultimate goal of the Straw Hat Pirates? ")
#     if question2.lower() == "find the One Piece":
#         print("Correct! Their goal is to find the One Piece treasure.")
#     else:
#         print("Wrong, it's to find the One Piece treasure.")

# else:
#     # For any other anime
#     print("I see you like", favorite_anime + ".")
#     print("Sorry, I don't have specific questions for that anime.")

# # End of the program
# print("Thanks for sharing your favorite anime with us!")
# -----------------------------------------------------

# print("")
# print("")


# Ask the user for their favorite Indian god or goddess
favorite_deity = input("Who is your favorite Indian god or goddess? ")

# Check the favorite deity and ask questions accordingly
if favorite_deity.lower() == "krishna":
    # Ask questions about Lord Krishna
    print("Great choice! Let's talk about Lord Krishna.")
    question1 = input("Who is Lord Krishna's divine consort? ")
    if question1.lower() == "radha" or question1.lower() == "radharani":
        print("That's correct! Radha is Lord Krishna's divine consort.")
    else:
        print("Oops, that's not correct. It's Radha.")

    question2 = input("In which scripture is Lord Krishna's story primarily found? ")
    if question2.lower() == "bhagavad gita" or question2.lower() == "mahabharata":
        print("Correct! Lord Krishna's story is primarily found in the Bhagavad Gita and Mahabharata.")
    else:
        print("Nope, it's in the Bhagavad Gita and Mahabharata.")

elif favorite_deity.lower() == "lakshmi":
    # Ask questions about Goddess Lakshmi
    print("Goddess Lakshmi is a wonderful choice! Let's talk about her.")
    question1 = input("What is the vehicle (vahana) of Goddess Lakshmi? ")
    if question1.lower() == "owl" or question1.lower() == "uluka":
        print("That's right! The owl is the vehicle of Goddess Lakshmi.")
    else:
        print("Incorrect. It's the owl (uluka).")

    question2 = input("During which festival is Goddess Lakshmi prominently worshipped? ")
    if question2.lower() == "diwali" or question2.lower() == "deepavali":
        print("Correct! Goddess Lakshmi is prominently worshipped during Diwali (Deepavali).")
    else:
        print("Wrong, it's during Diwali (Deepavali).")

elif favorite_deity.lower() == "hanuman":
    # Ask questions about Lord Hanuman
    print("Lord Hanuman is a powerful deity! Let's talk about him.")
    question1 = input("What is the other name for Lord Hanuman, which refers to his color? ")
    if question1.lower() == "sankat mochan":
        print("That's correct! Sankat Mochan refers to Lord Hanuman's color as the remover of troubles.")
    else:
        print("Oops, that's not correct. It's Sankat Mochan.")

    question2 = input("Which epic contains the story of Lord Hanuman's devotion to Lord Rama? ")
    if question2.lower() == "ramayana":
        print("Correct! The Ramayana contains the story of Lord Hanuman's devotion to Lord Rama.")
    else:
        print("Nope, it's the Ramayana.")

elif favorite_deity.lower() == "ganesha":
    # Ask questions about Lord Ganesha
    print("Lord Ganesha is a beloved deity! Let's talk about him.")
    question1 = input("What is the name of Lord Ganesha's vehicle (vahana)? ")
    if question1.lower() == "mouse" or question1.lower() == "mushika":
        print("That's right! Lord Ganesha's vehicle is a mouse (Mushika).")
    else:
        print("Incorrect. It's a mouse (Mushika).")

    question2 = input("What is the primary fruit associated with Lord Ganesha? ")
    if question2.lower() == "modak":
        print("Correct! The primary fruit associated with Lord Ganesha is the modak.")
    else:
        print("Wrong, it's the modak.")

else:
    # For any other deity
    print("I see you have an interest in", favorite_deity + ".")
    print("Sorry, I don't have specific questions for that deity.")

# End of the program
print("Thanks for sharing your favorite Indian god or goddess with us!")


#replit100DaysOfCode