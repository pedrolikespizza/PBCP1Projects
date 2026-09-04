# pedro bakare string notes

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
print(full_name.isalpha())
print(full_name.isupper())
print(full_name.isupper())

print(sentence.lower())
print(sentence.upper())
print(sentence.capitalize)
print(sentence.title())
print(fixed)
