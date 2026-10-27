# pb, period 1 password pseudocode project

'''
GET user input
 
IF user password has 8 or more characters
    score = 1
ELSE
    score = -1

IF user password has at least one uppercase
    score = 1
ELSE
    score = -1
    
IF user password has at least one number
    score = 1
ELSE score = -1

IF all three requirements are met, OUTPUT strong password

IF two out of the three requirements are met, OUTPUT medium password

IF one out of the three requirements are met, OUTPUT weak password

IF zero out of the three requirements are met, OUTPUT really weak password

'''