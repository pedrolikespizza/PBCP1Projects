# pedro bakare debugging notes


# syntax error
print("hello")
  # indentation error
if True:
  print("this is true") # <= identation error

people = 10
print(people)

#logic error
apples = 20
people = 3

print(apples * people )

#run time errors
while True:
  try:
    fav_num = int(input ("what is your favorite number"))
  except:
    print("thats not a number")
  else:
    break
        

print(4+ fav_num)