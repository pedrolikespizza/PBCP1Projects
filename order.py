# pb period 2 order project

food_choice = input(" what do you want to order:")

menu = {
"order": "burger, fries, sandwich, chicken tender, coke, sprite, lemonade",
    "burgers": "$5",
    "sandwich": "$3",
    "chicken tenders": "$2",
    "fries": "1", 
    "drink": "sprite",
    "drink": "coke",
    "drink": "lemonade",

}

keys = list(menu.keys())
values = list(menu.values())
for key in keys:
    print(f"{key} is  {menu[keys]}")

print(len(values))
print(len(keys))

text = print("this is your order:")