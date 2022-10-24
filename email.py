 import re
def data(name):
    if name.isalpha():
        email=input("enter your email")
        if emailval(email):
            print("your name is: " +name + "\n your email: " + email)
        else:
            print("this is not a vaild mail")
    else:
        print("this is not a string")
def emailval(email):
    reg="^[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*$"
    if re.search(reg,email):
        return True
    else:
        return False
name = input("enter your name")
data(name)
