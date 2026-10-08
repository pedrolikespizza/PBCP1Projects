# pb period 2 factorial calculator

import math
pedro_factorial = int(input("what number do you want the factorial of: "))

pedro_factorial = [pedro_factorial]
#apply map(math.factorial)
#turn it back into a list
#print the answer

math_fact = map(math.factorial,pedro_factorial)
new_list=list(math_fact)
print(*new_list)
#use list()