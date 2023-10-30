# Taking Lists to a New Dimension
# 2D lists..basically tables...will allow us to store more data like the cool kids.


# Check out my Bingo game for David (@lessonhacker)'s Nan! #thisOnesForDavidsNan Day 43 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python


# print("Take Your List To A New Dimension")
# print()

# my2DList = [ ["Jonnny",21, "Mac"],
#            ["Sina",19, "PC"],
#            ["Gethin",17, "PC"]]
# ________________
# print("Printing From a 2D List")
# print()
# print("the entire list")
# print()

# my2DList = [ ["Jonnny",21, "Mac"],
#  ["Sina",19, "PC"],
#  ["Gethin",17, "PC"]]

# print(my2DList)
# ________________
# print()

# print("a single row")
# print()

# my2DList = [ ["Jonnny",21, "Mac"],
#  ["Sina",19, "PC"],
#  ["Gethin",17, "PC"]]

# print(my2DList[0])

# ________________

# print("a single piece of data")
# print()

# my2DList = [ ["Jonnny",21, "Mac"],
#  ["Sina",19, "PC"],
#  ["Gethin",17, "PC"]]

# print(my2DList[0][1])

# ________________

# print("Editing a 2D List")
# print()

# my2DList = [ ["Jonnny",21, "Mac"],
#  ["Sina",19, "PC"],
#  ["Gethin",17, "PC"]]

# my2DList[0][2] = "Linux"

# print(my2DList[0])

# _____________________________________________________________________________

# print("Common Errors")
# print()

'''my2DList = [ ["Johnny", 21, "Mac"],
             ["Sian", 19, "PC"],
             ["Gethin", 17, "PC"] ]

print(my2DList[0][3])'''

''''Index out of range'?

👉 What is an 'out of range' error?'''

# my2DList = [ ["Johnny", 21, "Mac"],
#              ["Sian", 19, "PC"],
#              ["Gethin", 17, "PC"] ]

# print(my2DList[0][2])


# ________________

# print("Fix My Code")
# print()

'''my2DList =  ["Johnny", 21, "Mac"],
             ["Sian" 19, "PC"]
             ["Gethin", 17, "PC"], ]

print(my2DList[0][1])'''

# my2DList =  [ ["Johnny", 21, "Mac"],
#               ["Sian", 19, "PC"],
#               ["Gethin", 17, "PC"]
#             ]

# print(my2DList[0][1])


# ________________

print("👉 Day 43 Challenge")
print()

print("👉 Mecca Your Nan Very Happy")
print()
print("David's Nan's Bingo Card D+Generator")
print()

import random

bingo = []


def ran():
    number = random.randint(1, 90)
    return number


def prettyPrint():
    for row in bingo:
        print(row)


numbers = []
for i in range(8):
    numbers.append(ran())

numbers.sort()

bingo = [[numbers[0], numbers[1], numbers[2]],
         [numbers[3], "Bingo", numbers[4]],
         [numbers[5], numbers[6], numbers[7]]]

# print(bingo)
prettyPrint()


#replit100DaysOfCode