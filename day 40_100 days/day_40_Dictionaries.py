# Dictionaries
# Don't worry. No need to buy a massive paper book to look up words. Let's take lists one step further with dictionaries.



# I found a way to get your digits. Check out my address book. Day 40 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python



# print("Dictionaries")
# print()

# print("Creating a dictionary - brace!")
# dictName = {"name": "John", "age": 30, "city": "New York"}

# print("Printing the keys")
# print(dictName["name"])

# print("Changing an item")
# dictName["name"] = "The legendary John"
# print(dictName)

#________________________________________________________________________________________________________________

# print("Common Errors")
# print()
# print("Printing with keys and fStrings")
# print()

'''myUser = {"name": "David", "age": 128}

print(f"Your name is {myUser["name"]} and your age is {myUser["age"]}")'''

# myUser = {"name": "David", "age": 128}

# print(f"Your name is {myUser['name']} and your age is {myUser['age']}")

#_____________________________________

# print()
# print("Syntax error?")
# print()

'''myUser = {"name": "David", "age": 128}

print(myUser{"name"})'''

# myUser = {"name": "David", "age": 128}

# print(myUser["name"])

#_____________________________________

# print()
# print("Spare Key?")
# print()

'''myUser = {name:"David", "age": 128, "age" = 129}

print(myUser)'''

# myUser = {"name":"David", "age": 128}
# myUser["age"] = 129
# print(myUser)

#_______________________________________________________________________________________

# print("Fix My Code")
# print()
'''myUser = {name:"Andy", "age":128, "age" = 129}

print(myUser{"name"})'''

# myUser = {"name":"Andy", "age":128}
# myUser["age"] = 129
# print(myUser["name"])


#_______________________________________________________________________________________

print("👉 Day 40 Challenge")
print()

print("🌟Contact Card🌟")
print()
print()

name = input("Name: ").strip().capitalize()
dob = input("Date of Birth: ").strip()
tel = input("Telephone number: ").strip()
email = input("Email: ").strip()
address = input("Address: ")
contact = {"name": name, "dob": dob, "tel": tel, "email": email, "address": address}

print()
print(f"""Name: {contact["name"]}""")
print(f"""DOB: {contact["dob"]}""")
print(f"""Tel: {contact["tel"]}""")
print(f"""Email: {contact["email"]}""")
print(f"""Address: {contact["address"]}""")

#replit100DaysOfCode