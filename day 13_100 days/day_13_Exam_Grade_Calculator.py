# Gradebook Builder
# Whether you are a teacher or student, you can compute grades and generate your own gradebook with this project.


# first major project

print("Exam Grade Calculator")

examName = input("Name of Exam: ")
possibleScore = int(input("Max. Possible score: "))
yourScore = float(input("How many markd you got in exam/ Your Score: "))

percentage = (yourScore / possibleScore) * 100
percentage = round(percentage, 2)

# print("congrats you got",percentage,"%")

if percentage >= 90:
    print("congrats you got", percentage, "% in", examName, "and your grade is A+")

elif percentage >= 80 and percentage <= 89.99:
    print("congrats you got", percentage, "% in", examName, "exam and your grade is A-")

elif percentage >= 70 and percentage <= 79.99:
    print("congrats you got", percentage, "% in", examName, "exam and your grade is B")

elif percentage >= 60 and percentage <= 69.99:
    print("congrats you got", percentage, "% in", examName, "exam and your grade is C")

elif percentage >= 50 and percentage <= 59.99:
    print("congrats you got", percentage, "% in", examName, "exam and your grade is D")

elif percentage >= 40 and percentage <= 49.99:
    print("congrats you got", percentage, "% in", examName, "exam and your grade is E")

elif percentage <= 39.99:
    print("you got", percentage, "% in", examName, "exam and your grade is F, you'r fail try next fime good luck...")
else:
    print("Try again!")




#replit100DaysOfCode


# Built a grade calculator today! Definitely giving myself an A+ on this 😎 ! Day 13 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python