# pb while loops

# while loops keep running until a certain condtion is met

import random
import time

goose = random.randint(1,20)
duck = 1

while goose > duck:
    print("duck...")
    time.sleep(0.1)
    duck+=1
    if duck == 15:
        print("game over")
        break
else:
    print("GOOSE!")

# first part of the loop is the starting point
# second part of the loop is the boolean, it is also the end part 
# third part of the loop is the incrimentor, it is used to change our iterator
# iterator keeps track of the current iteration
#incrementer is what changes the iterator

count = 1
while count < 1:
    print(count)
    time.sleep(0.0001)
    count-=1



number = random.randint(1,101)

while True:
   
    while True:
        try:
            guess = int(input("guess a number between 1 and 100:"))
            break
        except:
            print ("that isn't a number")
    if guess == number:
       print("you win lil tung")
       break    
    elif guess < number:
        print("that number is too low")
    elif guess > number:
        print("that number is too high")    





       #continue restars the loop
       # break exits the loop 
       # else only happens if the loop ends naturally meaning if the condtion at the top becomes false, meaning the condtion ends
       # if you break out of a loop the else will not run