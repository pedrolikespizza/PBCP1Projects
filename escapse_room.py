# pb period escape room project

import sys  

print("You are trapped in tung tungs house enter a code on the door to escape:")
num_of_attempts = 0

while True:
    while True:
        try:
            code = int(input("what is the code: "))
            if code <= 0:
                ("Code is not a negative number")
                continue
        except ValueError:
            print("Not valid code try rentering")
        else:
            break

    if num_of_attempts == 0:
        if code == 6741:
            print("good job you did it")
            sys.exit()  
        else:
            print("try again. hint: password has 4 digits")
            num_of_attempts += 1

    elif num_of_attempts == 1:
        if code == 6741:
            print("good job you did it")
            sys.exit()   
        else:
            print("try again. hint: password has a 6 in it")
            num_of_attempts += 1

    elif num_of_attempts == 2:
        if code == 6741:
            print("good job you did it")
            sys.exit()  
        else:
            print("try again. hint: password has a 7 in it")
            num_of_attempts += 1

    elif num_of_attempts == 3:
        if code == 6741:
            print("good job you did it")
            sys.exit()  
        else:
            print("try again. hint: password has a 4 in it")
            num_of_attempts += 1

    elif num_of_attempts == 4:
        if code == 6741:
            print("good job you did it")
            sys.exit()  
        else:
            print("try again. FINAL hint: password has a 1 in it")
            num_of_attempts += 1

    elif num_of_attempts == 5:
        if code == 6741:
            print("good job you escaped tung tungs house! ")
            sys.exit()  
        else:
            print("try again. No more hints")

