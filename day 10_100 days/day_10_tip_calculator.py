

# Built my own tip calculator! Time to put it to the test at a restaurant 🍕 !  Day 10 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python



# print("")

# adding = 4+3
# print(adding)

# print("")

# Substration = 8 - 9
# print(Substration)

# print("")

# multiplication = 4 * 32
# print(multiplication)

# print("")

# division = 50 / 5
# print(division)

# print("")

# modulo = 15 % 4
# print(modulo)

# print("")

# divisor = 15 // 4
# print(divisor)

# print("")

# squared = 5**2
# print(squared)

# print("")

# adding = 4+3
# print(adding)

# print("")

#_________________________________________________________

# print("fixing broken code")

# print("")

'''👉 # Solve the following problems with my code
# Your goal is to print the solution of all 3 calculations to the screen.

# multiplication
3.4 * 6.8

# division
2467 / 4673

#raise 10 to the power of 2

# print the remainder when 343 is divided by 4
print("343 // 100")'''

# # multiplication
# multi = 3.4 * 6.8
# print("multiplication is: ",multi)

# print("")

# # division
# div = 2467 / 4673
# print("division is: ",div)

# print("")

# #raise 10 to the power of 2
# square = 10**2
# print("square is> ",square)

# print("")

# # print the remainder when 343 is divided by 4
# rem = 343 // 100
# print("remainder is: ",rem)

# print("")

#________________________________________________________

# print("Split the Bill ")

# print("")

# myBill = float(input("What was the bill?: "))

# print("")

# numberOfPeoples = int(input("How many peoples?: "))

# print("")

# answer = myBill / numberOfPeoples

# answer = round(answer, 2)

# print(answer,"for each of you hav to pay")

# _________________________________________________________________________________________


print("Tip Calculator")

print("")

totalBill = float(input("How much did you spend?: "))

numberOfPeople = int(input("How many people in your group?: "))

tipPercentage = float(input("What percentage do you want to tip?: "))

print("")

tip = (tipPercentage / 100) * totalBill
tip = round(tip,2)
print("Tip is: ", tip)

bill_with_tip = (tipPercentage / 100) * totalBill + totalBill
bill_with_tip = round(bill_with_tip, 2)

print("total bill with tip is: ", bill_with_tip,"Rs")

print("")

answer = bill_with_tip / numberOfPeople

answer = round(answer, 2)

print("You each own Rs", answer)

print("")
print("Thanks for comming..🥰")



#replit100DaysOfCode