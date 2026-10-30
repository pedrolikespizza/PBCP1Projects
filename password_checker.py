# pb period 1 password checker project.

password_1 = input("enter password for checking:")

length = len(password_1) >= 8

uppercase = any(char.isupper()for char in password_1)

lowercase = any(char.islower() for char in password)