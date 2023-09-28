# This is for me to learn how to make the calculator because I dont understand it.
print("Hi")
name = input('What is your name?' )
print(name)
print("Why won't this line of code print")
print('fixed ez')
print('This line fails too!')
print('ez')
print("I think I know how to fix this one")
print("ez")

name2 = input('Please tell me your name: ')
print(name2)
print('Blank line \nin the middle of string')
# /n makes a line mid sentence, crazy
first_name = input('What is your first name? ')
last_name = input('Now give me your last name. ')
print(first_name.capitalize() + ' ' + last_name.lower())
# .capatalize() gives the first letter capatal, and .lower makes the rest of it lowercase while the ' ' makes a word thats empty making it a space. i think
# variable.count(letter or number) counts the amount of time the thing in parathesis shows up
# challange thing time
n1 = input('give me a number ')
n2 = input('gimmie another ')
a1 = (float(n1) + float(n2))
print(a1)
#float makes it a number i think
print('hi\n\n\n\n\n\n\n\n\nbye')
# int is whole number and float is decimal
from datetime import datetime, timedelta
today = datetime.now()
print('Today is is: ' + str(today))
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was ' + str(yesterday))
bi1 = input('test number 1 ')
bi2 = input('test number 2 ')
print('put as a decimal or else money go bye bye')
tip = input('test tip 1 ')
tot = ((float(bi1) + float(bi2)) * (float(tip) + float(1)))
print(tot)
one_week = timedelta(weeks=1)
last_week = today - one_week
print('Fam last week was ' + str(last_week))
print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))

print('Hour: ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('Second: ' + str(today.second))

