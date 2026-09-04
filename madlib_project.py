#pedro bakare madlib project
name = input("Enter a person's name: ")
animal = input("Enter an animal: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")
food = input("Enter a food: ")

story = "One day, " + name + " went to " + place + " with a " + animal + ". "
story = story + "The " + animal + " was really " + adjective + " and started to " + verb + " around. "
story = story + name + " got hungry and pulled out some " + food + ". "
story = story + "The " + animal + " quickly grabbed the " + food + " and ran away. "
story = story + "Everyone at " + place + " laughed as " + name + " chased after the " + animal + "."

print(story)