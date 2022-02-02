# a215_multi_factor.py
import tkinter as tk
import multifactorgui as mfg
import re

# create a multi-factor interface to a restircted app
my_auth = mfg.MultiFactorAuth()

usercheck = False
while usercheck == False:
    username = input("Enter a username: ")
    if len(username) < 8:
        print("Your username must be greater than 8 characters")
    elif len(username) > 24:
        print("Your password must but shorter than 24 characters")
    elif len(username) > 8 and len(username) < 24:
        print("Your username is fine")
        usercheck == True
        break

passcheck = False
while passcheck == False:
    password = input("Enter a password: ")
    if len(password) < 8:
        print("Make sure your password is at lest 8 letters")
    elif re.search('[0-9]',password) is None:
        print("Make sure your password has a number in it")
    elif re.search('[A-Z]',password) is None: 
        print("Make sure your password has a capital letter in it")
    else:
        print("Your password seems fine")
        passcheck == True
        break

my_auth.set_authorization(username,password)
# confirm authorization info
auth_info = my_auth.get_authorization()
print(auth_info)

# set the users authentication information
question = "What is your favorite color?"
answer = "purple"
my_auth.set_authentication(question, answer)



 #start the GUI
my_auth.mainloop()
