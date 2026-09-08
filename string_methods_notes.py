# pedro bakare string notes
"""
sentence = "the quick brown fox jumps over the lazy dog"
fixed=sentence.replace("fox", "wolf")
#function would be finding the length len(sentence)  
#methods don't change the variable
#method sentence.lower()
#methods only work at the location you put them

word = input("what word do you want?:").strip().lower()
new_word = input("what word should be in the sentence:").strip().lower()
location = sentence.find(word)
new_sentence = sentence.replace(word,new_word)
print(sentence.find("over"))

first_name= input("what is your first name:").strip().title()

last_name= input("what is your last name:").strip().title()

first_seperated = first_name.split()

fixed= "".join(first_seperated)

last_seperated= last_name.split()

last_fixed= "".join(last_seperated)

full_name = fixed.title() + " " + last_fixed.title()

print("hello " + full_name.title())


print(full_name.isalpha()) #checks if the entire thing is characters
print(full_name.isnumeric()) # checks if the entire thing is numbers
print(full_name.isupper())# checks if all the string is uppercase


print(full_name.isupper()) # upper makes everything uppercase

print(sentence.lower()) # makes everything loweracase

print(sentence.upper())

print(sentence.capitalize) # capitalize the first letter

print(sentence.title())

print(fixed)



# formatted string lets easily us control the outputs for the user
print(f"hello{first_name} {fixed.title} {last_name} welcome to my program")"""

letter = input("give me a letter: ")
letter + letter[0].lower()
number_value = ord(letter) # ord gives you order of the number
number_value += 2
new_letter = chr(number_value) # chr makes
print(f"your letter was {letter} now it is {new_letter}")
