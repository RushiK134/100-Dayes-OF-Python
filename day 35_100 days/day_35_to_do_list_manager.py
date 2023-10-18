# The ULTIMATE List Maker
# Beef up your to do list from Day 33 to make the ULTIMATE list maker by adding 'pretty printing' subroutines.



# My to do list organizer from Day 35 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python




import os, time
print("👉 Day 35 Challenge")
print()

print("to do list manager")
print()


toDoList = []

def printList():
  print()
  for item in toDoList:
    print(item)
  print()

while True:
  menu = input("ToDoList Manager\n\nDo you want to view, add, edit, remove or delete the todo list?\n").lower()
  if menu=="view":
    printList()
  elif menu=="add":
    item = input("What do you want to add?\n").title()
    toDoList.append(item)
  elif menu=="remove":
    item = input("What do you want to remove?\n").title()
    check = input("Are you sure you want to remove this?\n".lower())
    if check[0] == 'y':
      if item in toDoList:
        toDoList.remove(item)
  elif menu == "edit":
    item = input("What do you want to edit?\n").title()
    new = input("What do you want to change it to?\n").title()
    for i in range(0,len(toDoList)):
      if toDoList[i] == item:
        toDoList[i] = new
  elif menu == "delete":
    toDoList = []
  time.sleep(1)
  os.system("clear")





#replit100DaysOfCode