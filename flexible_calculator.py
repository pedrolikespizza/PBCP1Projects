# pb flexible calculator project

import math

def get_type(question, *math_type):
    while True:
        math_choice = input(question)
        if get_type in math_type:
            return get_type
        else:
            print(" not one of the options. spell it right or pick one of the options that are displyed lil tung")
def get_num():
    print("put in a number, then when your done putting in your number type done")
    number = []
    while True:
        user_1 = input("what number do you wanna calculate: ")
        if user_1 == "done":
            break
        try:
            number.append(float(user_1))
        except ValueError:
            print("incorrect input enter a vaild number or enter any letter")
            return number
def calc(operation, *numeros):
    if operation == "sum":
        return sum(numeros)
    elif operation == "average":
        return sum(numeros)/ len(numeros)
    elif operation == "max":
        return max(numeros)
    elif operation == "min":
        return min(numeros)
    elif operation == "product":
        return math.prod(numeros)


math_type = get_type("what operation do you want to do. (sum, average, max, min, product)" )
    
user_number = get_num()

if len(user_number) == 0:
    print("not a vaild input, no number was entered")
else:
    end_product = calc(get_type, *user_number)
    print(f"{get_type}: {end_product}")
        