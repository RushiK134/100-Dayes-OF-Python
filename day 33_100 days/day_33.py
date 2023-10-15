# Getting Dynamic
# For all you list makers, this lesson is for you. With dynamic lists, create a working to do list to keep yourself on track.


# This one is for all the list makers. Built a customized to do list today. ✅ Day 33 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python


# print("Dynamic Lists")
# print()

# myAgenda = []

# def printList():
#   print()
#   for item in myAgenda :
#     print(item)
#   print()
# while True:
#   item = input("What's next on the Agenda?: ")
#   myAgenda.append(item)
#   printList()

#_________________________________________________________________________

# print("Removing Items from a List")
# print()


#   myAgenda = []

#   def printList():
#     print()
#     for item in myAgenda:
#       print(item)
#     print()

#   while True:
#     menu = input("add or remove?: ")
#     if menu == "add":
#       item = input("What's next on the Agenda?: ")
#       myAgenda.append(item)
#     elif menu == "remove":
#       item = input("What do you want to remove?: ")
#       myAgenda.remove(item)
#     printList()

#______________________________________________________________________________________________

# print("Common Errors")
# print()

'''myAgenda = []

def printList():
  print()
  for item in myAgenda:
    print(item)
  print()

while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    myAgenda.append(item)
  elif menu == "remove":
    item = input("What do you want to remove?: ")
    myAgenda.remove(item)
  printList()'''

# myAgenda = []

# def printList():
#   print()
#   for item in myAgenda:
#     print(item)
#   print()

# while True:
#   menu = input("add or remove?: ")
#   if menu == "add":
#     item = input("What's next on the Agenda?: ")
#     myAgenda.append(item)
#   elif menu == "remove":
#     item = input("What do you want to remove?: ")
#     if item in myAgenda:
#       myAgenda.remove(item)
#     else:
#       print(f"{item} is not in the list")")
#   printList()




'''myAgenda = []

def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 

while True:
  menu = input("Add or Remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    item.append(myAgenda)
  elif menu == "remove":
    item = ("What do you want to remove?: ")
    if item in myAgenda:
      item.remove(myAgenda)
    else:
      print(f"{item} was not in the list")
  printList()'''


# myAgenda = []

# def printList():
#   print()
#   for item in myAgenda:
#     print(item)
#   print()

# while True:
#   menu = input("Add or Remove?: ")
#   if menu == "add":
#     item = input("What's next on the Agenda?: ")
#     myAgenda.append(item)
#   elif menu == "remove":
#     item = ("What do you want to remove?: ")
#     if item in myAgenda:
#       myAgenda.remove(item)
#     else:
#       print(f"{item} was not in the list")
#   printList()


#_______________________________________________________________

# print("Fix My Code")
# print()
'''def printList():
  print() 
  for item in myPartyList:
    print(item)
  print() 

while True:
  menu = input("add or remove?: )
  if menu = "add":
    item = input("Who should I add to the party list?: ")
    myPartyList.add(item)
  elif menu == "remove":
    item = input("Who should I remove from the party list?: ")
    if item in myPartyList:
      myPartyList.remove(list)
    else:
      print("{item} was not in the list)
  printList()'''

# myPartyList = []
# def printList():
#   print()
#   for item in myPartyList:
#     print(item)
#   print()

# while True:
#   menu = input("add or remove?: ")
#   if menu == "add":
#     item = input("Who should I add to the party list?: ")
#     myPartyList.append(item)
#   elif menu == "remove":
#     item = input("Who should I remove from the party list?: ")
#     if item in myPartyList:
#       myPartyList.remove(item)
#     else:
#       print(f"{item} was not in the list")
#   printList()


#___________________________________________________________________

print("👉 Day 33 Challenge")
print()

import os, time
toDoList = []

def printList():
  print()
  for item in toDoList:
    print(item)
  print()

while True:
  menu = input("ToDoList Manager\n\nDo you want to view, add or edit the todo list?\n")
  if menu=="view":
    printList()
  elif menu=="add":
    item = input("What do you want to add?\n")
    toDoList.append(item)
  elif menu=="edit":
    item = input("What do you want to remove?\n")
    if item in toDoList:
      toDoList.remove(item)

#replit100DaysOfCode