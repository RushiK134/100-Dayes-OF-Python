# "525,600 minutes"
# 525,600 minutes. Now, use your newfound math skills to determine how many seconds are in a year.


# day_11 Project day! How many seconds in a year
'''60 seconds = 1 minute
60 minutes = 1 hour
24 hours = 1 day
31 days = 1 month
12 months = 1 year
365 days = 1 year
366 day = 1 leap year (this is every four years) '''


days_current_year = int(input("How menty days are in current year: "))

print("")

days_in_year = 365
days_in_leapyear = 366
hours_in_day = 24
minuts_in_hour = 60
seconds_in_minute = 60

for_year = days_in_year * hours_in_day * minuts_in_hour * seconds_in_minute

for_leapyear = days_current_year * hours_in_day * minuts_in_hour * seconds_in_minute


if days_current_year == 365:
  print("Number of seconds in a year are", for_year)
elif days_current_year == 366:
  print("Numbers of seconds in leaf year are", for_leapyear)
else:
  print("yeee.. baba yesa konsa sal hai re jisme",days_current_year,"din hai.  Ja re Ja re baba tu....")

#replit100DaysOfCode



# How many seconds in a year 🙀 !! Day 11 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python