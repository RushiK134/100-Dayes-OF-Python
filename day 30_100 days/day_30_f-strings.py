# f...what?
# The `f` stands for format...not whatever you were thinking. Change the way you combine strings and variables with f-strings.

# Reflecting on my amazing work from the last 30 days. Created a reflection journal 📓. Day 30 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python




# print("f-strings")
# print()

# name = "Kartik"
# age = "28"
# pronouns = "she/her"
# print("My name is {},using {} pronouns and is age, {}".format(name,pronouns,age))

#________________________________________________________________________________________

# print()
# print("Local Variables")
# print()
# name = "Katie"
# age = "28"
# pronouns = "she/her"

# # print("This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age))


# response = "This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age)

# print(response)

#____________________________________________________________________________


# print()
# print("The Power of f...")
# print()

# name = "Katie"
# age = "28"
# pronouns = "she/her"

# response = f"This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far"

# print(response)


#____________________________________________________________________________________

# print()
# print("Alignment")
# print()
'''left = <, right = >, center = ^'''
# for i in range(1,11):
#   print(f"Day {i:} of 11")

# for i in range(1,11):
#   print(f"Day {i: <2} of 11")

# for i in range(1,11):
#   print(f"Day {i: >3} of 11")

# for i in range(1,11):
#   print(f"Day {i: ^3} of 11")

#____________________________________________________________________________________

# print()
# print("Fix My Code")
# print()

'''food = pizza"
location = "beach"
color = "green"
friend = "Quinn"

"Alejandra ordered {food} to eat at the {location} with her friend, {friend}. She got to the {location} and looked for a {color} umbrella where {friend} said they would be waiting. By the time, Sally found {friend}, the {food} was cold and the {location} was lame." format(food=food, location=location, color=color,)

print(response)'''

# food = "pizza"
# location = "beach"
# color = "green"
# friend = "Quinn"

# response ="Alejandra ordered {food} to eat at the {location} with her friend, {friend}. She got to the {location} and looked for a {color} umbrella where {friend} said they would be waiting. By the time, Sally found {friend}, the {food} was cold and the {location} was lame." .format(food=food, location=location,friend = friend, color=color,)

# print(response)

#_______________________________________________________________________________

print("👉 Day 30 Challenge")
print()
print("30 Days Down - What did you think?")
print()

for i in range(1,31):
  userThink = input(f"Day {i}:\n")
  print()
  me = f"You thought Day {i} was"
  print(f"{me: ^38}")
  print(f"{userThink: ^38}")
  print()



#replit100DaysOfCode