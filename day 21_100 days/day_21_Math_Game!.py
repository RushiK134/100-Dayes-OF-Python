# Throwback to Math Facts
# Create a game to test your friends’ knowledge on their math facts.

# Let's multiply on the floor. Why? Because you can't use tables 😁. Day 21 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python


print("👉 Day 21 Challenge")
print()
print("Math Game!")
print()
print("Welcome to Math Facts Game")
print()
print("How well do you know your math facts? Pick a number and I will give you 10 math facts to solve.")
print()


# print("Thirteen Times Table")
# for i in range(1,13):
#   print(i, "x 13 =", i*13)


n = int(input("Name your multiples: "))
point = 0
for i in range(1,11):
  correct_ans = i*n

  print(i,"x",n)
  answer = int(input(":- "))
  if answer == correct_ans:
    print("Great work! ")
    point += 1
  else:
    print("That's not correct. It should have been", correct_ans)

if point == 10:
  print("Wow! A perfect score! 🥳")
else:
  print("You got", point, "out of 10 correct.")


#replit100DaysOfCode