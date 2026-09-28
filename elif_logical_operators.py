# pb, elif and logical operators notes
'''
age = 14

if age >= 18:
    print("you are an adult and can vote!")
elif age >= 15:    
    print("you can drive if you have the right paperwork") 
else:

    print("you are too young to drive")
'''

# all conditionals start with if
# elif's are inbetween
# else mars the end of the conditional
# elif only happens if the condtionals above it are false
#logical operators are and, or, and not
# and is both boolean statements must both be true
# or is at least one must be True
# not means the next boolean statement will be false

win = True
hp = 25

if win or hp < 1:
    
    print("game over")
    
else:
    print("the game is still going")