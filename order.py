# pb period 2 order project

# menu makes it a dictionary
menu = {
    "main": {
        "cheese burger": 3.50,
        "burrito": 5,
        "sandwich": 2.50,
        "hot dog": 1.50
    },
    "side": {
        "fries": 1,
        "hashbrowns": 1.5,
        "mac and cheese": 3,
        "tater tots": 2.5
    },
    "drinks": {
        "sprite": 1.5,
        "coka cola": 1.5,
        "lemonade": 1.5,
        "water": 0,
        "apple juice": 0,
        "fruit punch": 1.5
    },
}

# prints the menu and options for food
print(" Main Course Options ")

print(*menu["main"])

print(" side course options ")

print(*menu["side"])

print(" drinks course options ")

print(*menu["drinks"])

#makes function that asks the user their order
def get_order(question, catorgory):
    while True:
        food_choice = input(question).lower()
        if food_choice in menu[catorgory]:
            return food_choice
        else:
            print("try again lil tung you need to spell as spelled on menu")
            continue

# uses the function to get their order
main_food = get_order("what main course do you want: ", "main")
side1_food = get_order("what do you want your first side to be: ", "side")
side2_food = get_order("what do you want your second side to be: ", "side")
drink_food = get_order("what drink do you want: ", "drinks")

# gets total based on their order
main_price = menu["main"][main_food]
side1_price = menu["side"][side1_food]
side2_price = menu["side"][side2_food]
drink_price = menu["drinks"][drink_food]
total = main_price + side1_price + side2_price + drink_price

# printsther order and total
print("your order is:")
print(f"main: {main_food}")
print(f"side 1: {side1_food}")
print(f"side 2: {side2_food}")
print(f"drink: {drink_food}")
print(f" your total is: ${total}") 