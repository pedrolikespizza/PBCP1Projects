# pb period 1 password checker project.

password = input("enter a password for checking: ")

length_check = len(password) >= 8

uppercase_check = any(char.isupper() for char in password)

lowercase_check = any(char.islower() for char in password)

number_check = any(char.isdigit() for char in password)

special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"

special_check = any(char in special_characters for char in password)


score = 0

if length_check:
    score += 1

if uppercase_check:
    score += 1

if lowercase_check:
    score += 1

if number_check:
    score += 1

if special_check:
    score += 1


if score <= 2:
    strength = "weak, do better dude."
elif score == 3:
    strength = "medium"
elif score == 4:
    strength = "strong"
else:
    strength = "very strong, good job lil tung!"


print("Password strength assessment:")
print("length (8+ characters):", "yes" if length_check else "no")
print("contains uppercase:", "yes" if uppercase_check else "no")
print("contains lowercase:", "yes" if lowercase_check else "no")
print("contains numbers:", "yes" if number_check else "no")
print("contains special characters:", "yes" if special_check else "no")

# Display final score and strength
print("strength score:", str(score) + "/5")
print("password strength:", strength)