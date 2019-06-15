# Problem 1 :
#  Create a program that asks the user to enter their name and their age.
#  Print out a message that will tell them the year that they will turn 95 years old.

#!/usr/bin/python3

name = input('Your Name:- ')
age = int(input('Your age:- '))
year = 95 - (age)
print(f'{name } will turn ', 2019 + year)

