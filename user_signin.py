# pb user sign in project

"""
correct_username="username"
correct_password="password"

CHECK if their username input is the same as correct_username
    IF PASS, continue to password input
    ELSE, ask for username input again
CHECK if their password input is the same as correct_password
    IF PASS, say they signed in
    ELSE, loop to the beginning
"""

correct_username = ("tung tung")
username_input = input("what is your username lil tung: ")
correct_password = ("6741")
password_input = input("what is your password lil tung: ")

if correct_username == username_input:
    print("correct username")
    if correct_password == password_input:
        print("correct password")
        print("welcome pedro")
    else:
        print("who do you think you are?")
else:
    print("who do you think you are?")        