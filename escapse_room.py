# pb period escape room project

import sys  

print("You are trapped in tung tungs house enter a code on the door to escape")

while True:
    try:
        code = int(input("what is the code: "))
        if code >= 0:
            break
        elif code <= 0:
            ("Code is not a negative number")
    except ValueError:
        print("Not valid code try rentering")
    else:
        print("Not a valid code renter")

while True:
    if code == 6741:
        print("good job you did it")
        sys.exit()  
    else:
        print("try again. hint: password has 4 digits")
        break  

while True:
    if code == 6741:
        print("good job you did it")
        sys.exit()   
    else:
        print("try again. hint: password has a 6 in it")
        break

while True:
    if code == 6741:
        print("good job you did it")
        sys.exit()  
    else:
        print("try again. hint: password has a 7 in it")
        break

while True:
    if code == 6741:
        print("good job you did it")
        sys.exit()  
    else:
        print("try again. hint: password has a 4 in it")
        break

while True:
    if code == 6741:
        print("good job you did it")
        sys.exit()  
    else:
        print("try again. FINAL hint: password has a 1 in it")
        break

while True:
    if code == 6741:
        print("good job you did it")
        sys.exit()  
    else:
        print("try again. No more hints")
