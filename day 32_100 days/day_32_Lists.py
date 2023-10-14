# Make a List
# Learn how to store more than one piece of information in a single variable with the power of lists.


# Built a random greetings list to greet you in different languages 👋. Day 32 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python




# print("Lists")
# print()
# print("Printing Lists")
# print()

# timetable = ["Computer Science","Math","English","Art","Sport"]
# print(timetable[0])
# print(timetable[1])
# print(timetable[2])
# print(timetable[3])
# print(timetable[4])


# print("Changing Lists")
# print()
# timetable[4] = "Whatch TV"
# print(timetable[0])
# print(timetable[1])
# print(timetable[2])
# print(timetable[3])
# print(timetable[4])

#_____________________________________________________________________

# print("Lists and Loops")
# print()
# timetable = ["Computer Science","Math","English","Art","Sport"]
# for lesson in timetable:
#   print(lesson)

#___________________________________________________________________________


# print("Common Errors")
# print()

'''colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
print(f"The first color is {colors[1]}")'''


# colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
# print(f"The first color is {colors[0]}")

'''colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
print(f"The last color is {colors[6]}")'''

# colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
# print(f"The last color is {colors[5]}")

#______________________________________________________________________________________

# print("Fix My Code")
# print()

'''grocery list = ["bananas", "bread", "milk", "eggs", "juice", "cheese"]
print("The first grocery item to buy is {grocery list[1]}.")'''

# grocery_list = ["bananas", "bread", "milk", "eggs", "juice", "cheese"]
# print(f"The first grocery item to buy is {grocery_list[0]}.")

#__________________________________________________________________________

print("👉 Day 32 Challenge")
print()
'''
    Marathi: नमस्कार (Namaskar)
    English: Hello
    Spanish: Hola
    French: Bonjour
    German: Hallo
    Italian: Ciao
    Portuguese: Olá
    Russian: Привет (Privet)
    Chinese (Mandarin): 你好 (Nǐ hǎo)
    Japanese: こんにちは (Konnichiwa)
    Arabic: مرحبًا (Marhaban)
    Hindi: नमस्ते (Namaste)
    Dutch: Hallo
    Korean: 안녕하세요 (Annyeong haseyo)
    Turkish: Merhaba
    Swedish: Hej
    Greek: Γειά σας (Yia sas)
    Vietnamese: Xin chào
    Hebrew: שלום (Shalom)
    Swahili: Jambo
    '''
import random

langGreet = ["नमस्कार","Hello","Bonjour","Hallo","Hola","Ciao","Olá","Privet","Nǐ hǎo","Konnichiwa","Marhaban","Merhaba","Hej","Annyeong haseyo","Yia sas","Shalom","Jambo"]

# randomGreet = random.randint(0,len(langGreet)-1)
# print(langGreet[randomGreet])

# print(len(langGreet))
randomGreet = random.randint(0,len(langGreet)-1)

colours = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m","\033[0m"]

randomcol = random.randint(0,len(colours)-1)

print(colours[randomcol],langGreet[randomGreet])





#replit100DaysOfCode