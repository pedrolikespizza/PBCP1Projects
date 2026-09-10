# pedro bakare dice roller asignment
import random
dice_input=input("what dice do you want to roll? your options are D4, D6, D8, D10, D12, D20:")
if "4" in dice_input:
    dice_input=4
elif "6" in dice_input:
    dice_input=6
elif "8" in dice_input:
    dice_input=8
elif  "10" in dice_input:
    dice_input=10
elif  "12" in dice_input:
    dice_input=12
elif  "20" in dice_input:
    dice_input=20 
dice= random.randint(1,dice_input)
print(f"you rolled {dice}!")