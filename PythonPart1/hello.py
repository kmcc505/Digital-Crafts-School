'''
#problem 1
name = input('What is your name? ')
print("Hello," +name +"!")
#problem 2
name = input('What is your name? ')
print("Hello," +name +"!")
print("Your Name Has", len(name), "LETTER IN IT! AWESOME!")
#problem 3
#input ("name", "subject")
name = input("What is your name")
subject = input("What is the subject")
print(name + "'s favorite subject in school is" + subject)

#problem 4
#day = int(input('Day (0-6)? '))
week = ["Sunday", "Monday", "Tuesday", "Wednesday," "Thuesday", "Friday", "Sunday"]
day_of_week =int(input("Please give day of the week (0-6) 0 is Sunday."))
print(week[day_of_week])

#problem 5
week = ["Sunday", "Monday", "Tuesday", "Wednesday," "Thuesday", "Friday", "Sunday"]
day_of_week =int(input("Please give day of the week (0-6) 0 is Sunday."))
if day_of_week == 0 or day_of_week ==6:
    print("Sleep in")

if day_of_week >=1 and day_of_week<=5:
    print("Go to work")

#problem 6
tempc = int(input("Tempature in C")) 
tempf = tempc * 1.8 + 32
print(tempf)
'''
#problem 7
total = int(input("What is the total bill"))
rating = input("level of service? [put good, fair, or bad]")
level_of_service = ("good", "fair", "bad")
if rating == ("good"): 
   tip = total *.2
   total = total + tip
   print(total)
elif rating == "fair":
    tip = total *.15
    total = total + tip
    print(total)
else:
    tip = total *.1
    total = total + tip
    print(total)

       