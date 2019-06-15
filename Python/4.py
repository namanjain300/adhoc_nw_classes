# Problem 4:  

# take all input from user .

# i)  check that all character are string
# ii)  if all char are string then create user in your linux based OS
# iii)  also create password for same user , password will
#       password will be  ===>>     hello{username}

#!usr/bin/python3
import os
import crypt
var1= input("Enter your Username:- ")
try:
    val = str(var1)
    print("That is a string")
except ValueError:
    print("That is not a string")

os.system(f"useradd -p $(openssl passwd -1 hello{var1}) {var1}")



