# What Can Range really do?
# Bring on the start of list making by learning all the capabilities of range.

# What are ten things you can always count on? Your fingers. Or this number generator I made.  Day 20 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python



# print("What can range really do?")
# print()
# print("starting value: what number do you want to start with?")
# print()
# print("ending value: the number after the number you want to end with (example: if you type 10 as the ending value, the computer will count until 9)")
# print()
# print("increment: How much should it increase by every time it loops? (example: Do you want to count by 1s, 5s, 10s?)")

# print("")
# print("starting value and ending value")
# for i in range(100,110):
#   print(i)

# print("")
# for i in range(1,8):
#   print("Day", i)

# print("")

# print("Thirteen Times Table")
# for i in range(1,13):
#   print(i, "x 13 =", i*13)

# print("")
# print("starting value,ending value and increment")
# print("Increments")
# for i in range(0,1000000,25):
#   print(i)

# print()
# print("Counting Backward")
# print("")

# for i in range(10,0,-1):
#   print(i)

# print()
# print("Common Errors")

'''for i in range(10,0):
  print(i)'''
# for i in range(10,0,-1):
#   print(i)

# print("Fix My Code")
# print()
# '''for i in range(20,40,-1):
#   print(i)'''
# for i in range(20,40,1):
#   print(i)

print()

print("👉 Day 20 Challenge")
print("")
print("List Generator")
print()

print("Welcome to my number list generator.")
print()
print("You are going to give me a number you want to start with, an ending number, and by how many you want me to add each time.")
print()

startNo = int(input("Enter Starting number: "))
endNo = int(input("Enter Ending number: "))
increment = int(input("Enter Increment between values: "))
for i in range(startNo,endNo,increment):
  print(i)


#replit100DaysOfCode