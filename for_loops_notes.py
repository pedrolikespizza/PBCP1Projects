# pb for loops notes
import time
#time is a libary of permade funcs that we can use
# iteration means we do the same thing to every item in a list/collection
siblings = ["alex", "tung tung", "67"]
for sibling in siblings:
    print(f"goooood morning {sibling}!")



grades = [100, 87, 53, 45, 78, 72, 88, 3, 94]
average = 0

for grade in grades:
    average += grade
    print(f"{grade} was added.")




average = average/len(grades)   
print(f"the average grade is {average:.2f}")



# the first number in the parenthesis is the number we start at, the second number is where we end, the last number is what we count by
for i in range (2,21,2):
    print(i)
    time.sleep (1)


for i in range(20, 0, -1):
    print(i)
    time.sleep(1)
    if i == 12:
        print("wait is it lunch time")
        break














#/t helps us line up things properly


# for is for for loop
# the word next to the for is our iterater variable, how we know if it's our iterater varible is if it is the single version of a variable.
# i
# range builds a list for you