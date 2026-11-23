# pb flexible calculator project

import math

def get_type(question, *math_type):
    while True:
        math_choice = input(question)
        if get_type in math_type:
            return get_type
        else:
            print(" not one of the options. spell it right or pick one of the options that are displyed lil tung")