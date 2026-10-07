# pb mapping notes osns



# mapping takes a list and applys a function to a list

import math

def times(number):
    return number *2

numbers = range(1,6)

multiplied_numbers = map(times,numbers)

print(list(multiplied_numbers))


# pointer means we have to go to a certain location

# map takes in 2 pieces of info. the function name we are running, and the list
new_numbers = []
for number in numbers:
    new_numbers.append(number*2)

print(*new_numbers)

siblings = ["alex", "katie", "hugo", "salesi", "67", "triplet"]

length = list(map(len, siblings))
print(length)

print(math.factorial(5))