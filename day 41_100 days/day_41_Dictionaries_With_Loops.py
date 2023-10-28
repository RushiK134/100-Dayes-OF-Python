# I've Lost My Keys
# Dictionaries and loops are not always friends. Discover the secret to ensuring they get along.


# It's 5 stars for me. ✨ Use my project to rate your favorite websites. Day 41 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python


# print("Dictionaries With Loops")
# print()

# print("I've Lost My Keys!")
# print()

'''👉 Using a for loop, like we would with a list, will output the values, but not the keys. Not ideal.'''
# myDictionary = {"name":"Ian","health":219, "strength": 199, "equipped": "Axe"}
# for i in myDictionary:
#   print(myDictionary[i])

# ___
'''👉 This loop uses the .values() method, which can be run on a data type. We still only get the value, and not the key.'''
# myDictionary = {"name":"Ian","health":219, "strength": 199, "equipped": "Axe"}
# for value in myDictionary.values():
#   print(value)

# ______________________________________________

# print("I've Got The Key...I've Got The Secret")
# print()

'''👉 The .items() function returns the key name and value. Note that I've supplied the loop with two arguments: 'name' and 'value').'''

# myDictionary = {"name":"Ian","health":219, "strength": 199, "equipped": "Axe"}
# for name,value in myDictionary.items():
#   print(f"{name}: {value}")


# ______________________________________________

# print("A Bit Iffy")
# print()

'''Let's go one step further and use some if statements inside the loop.'''

# myDictionary = {"name":"Ian","health":219, "strength": 199, "equipped": "Axe"}
# for name,value in myDictionary.items():
#   print(f"{name}: {value}")
#   if (name == "strength"):
#     print("Whoa, I'm so strong!")
# __________

'''👉This example uses nested if statements to react to the key name and the value stored within it.'''

# myDictionary = {"name":"Ian","health":219, "strength": 199, "equipped": "Axe"}
# for name,value in myDictionary.items():
#   print(f"{name}: {value}")

#   if (name == "strength"):
#     if(value>100):
#       print("Whoa, I'm so strong!")
#     else:
#       print(f"I'm weak. I'm only {value} units.")

# __________________________________________________________________


# print("Common Errors")
# print()

'''Make The Brackets Go Away!'''

'''myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for name in myDictionary.items():
  print(f"{name}")'''

# myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

# for name,value in myDictionary.items():
#   print(f"{name} {value}")


# __________________________________________________________________


# print("Fix My Code")
# print()

'''myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

for name in myDictionary.items():
  print(f"{name}:{value}")

  if (name == "strength"):
  if value > 100:
    print("Whoa, SO STRONG")
  else:
    print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")'''

# myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

# for name,value in myDictionary.items():
#   print(f"{name}:{value}")

#   if (name == "strength"):
#     if value > 100:
#       print("Whoa, SO STRONG")
#     else:
#       print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")


# __________________________________________________________________


print("👉 Day 41 Challenge")
print()

print("🌟Website Rating🌟")
print()
print()

name = input("Input the website name: ").strip().capitalize()
print()

url = input("Input the URL: ").strip()
print()

desc = input("Input your a description: ").strip()
print()

rating = input("Input the a star rating out of 5: ").strip()
print()

myDictionary = {"name": name, "url": url, "desc": desc, "rating": rating}

print()
print()

for name, value in myDictionary.items():
    print(f"{name}:{value}")

# website = {"name": None, "url": None, "desc": None, "rating": None}

# for name in website.keys():
#   website[name] = input(f"{name}: ")

# print()
# for name, value in website.items():
#   print(f"{name}: {value}")


#replit100DaysOfCode