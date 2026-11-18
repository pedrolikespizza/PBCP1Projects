# pb period 2 order project

food_choice = input(" what do you want to order:")

menu = {
"main course 1": "cheeseburger",
"main course 2": "burrito",
"side 1": "fries",
"side 2": "mac and cheese",
"drink 1": "sprite",
"drink 2": "lemonade",
}

keys = list(menu.keys())
values = list(menu.values())
for key in keys:
    print(f"{key} is  {menu[keys]}")

print(len(values))
print(len(keys))

text = print("this is your order:")