import re

def length_dector(password):
    if len(password) >= 8:
        return True
    else:
        print("Please input a password longer than 8.")

def upper_dector(password):
    upperRegex = re.compile(r'[A-Z]')
    if upperRegex.search(password) == None:
        print("Please make sure the password includes an UPPER case.")
    else:
        return True

def lower_dector(password):
    lowerRegex = re.compile(r'[a-z]')
    if lowerRegex.search(password) == None:
        print("Please make sure the password inclues a lower case.")
    else:
        return True

def number_dector(password):
    numberRegex = re.compile(r'[0-9]')
    if numberRegex.search(password) == None:
        print("Please make sure the password includes a number")
    else:
        return True

def strong_password_dector(password):
    if length_dector(password) and upper_dector(password) and lower_dector(password) and number_dector(password):
        return password
    else:
        return False

password = []
active = True
while active:
    password = input("Please input a strong password which is longer thant 8 and also includes an upper case, a lower case, and a number: ")
    if strong_password_dector(password):
        active = False
        print("Congratulation, your password meets the requirement.")

print(password)
        
