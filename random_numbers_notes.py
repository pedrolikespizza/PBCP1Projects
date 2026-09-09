# pedro bakare random numbers notes

# random does not exsit in the programming world
#random is a key word


#arugement 1 is lowest number, arugement 2 is the highest number. arugements are the info that we give the function to make it run
#function is a code that was already built that we can use by calling its name


#randit lets us get a random integer

import random
ducks = random.randint(1,10)
print(f"there are {ducks} ducks!")


#computer needs a number for a random number
#notrandom gives us a specifc number
#return is the info that is given back
# random.choice is making a choice between the variables, arugements


pens = random.randrange(2,10,2)
print(f"i have {pens} pens. ")


# even number at the end makes all numbers even, uneven numbers make all nubmers uneven
# the last number makes the numbers even. and it counts by that much numbers aswell
#the middle number is the limit for numbers
#the first number is the starting point

percent = random.random()
print(f"you gave a {percent:.2} grade. ")


#random.random gives us a float that is between 1 and 0
# the :.2 makes the number looks like what is should