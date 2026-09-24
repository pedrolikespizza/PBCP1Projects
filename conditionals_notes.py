# pedro bakare conditional notes

# to write a conditional you start with if
#conditionals always start with if, then you write the boolean statement, then we have to end it in a colon
#anytime a line ends with a colon, the next line has to be indented
#else is for any other instance
grade = 64
if grade >= 90:
    print("you have an A! good stuf lil tung")  
elif grade >= 70:
    print("you are passing!")
else:
    print("you are not passing lil tung")
    print("do you need to retake a quiz? or do you need to submit a missing assignment?")
    
raining = False

if raining:
    print("bring an umbrella")
else:
    print("wear sunscreen")    