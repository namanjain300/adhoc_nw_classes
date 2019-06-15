# Problem 5:

# write a code  will take  input as your name and greet you with
# good morning , good evening , goodafter noon , good night as per the current time your system :

#!usr/bin/python3
import time
name= input("What's your name: ")
curtime=int(time.strftime('%H'))
if curtime < 12 :
    print('Good Morning ' +name)
if curtime > 12 and curtime < 18 :
    print('Good Afternoon ' + name)
if curtime > 18 and curtime < 22 :
    print('Good Evening ' +name)
if curtime > 22 :
    print('Good Night ' +name)