# pb dictonaries notes

# collection of key value paris

car = {
"make": "jeep", 
"modle": "wrangler",
"color": "silver",
"year":2023
}

keys = list(car.keys())
for key in keys:
    print(f"{key} is {car{key} }")




print(len(car))
if "transmission" in car:
    print(car{"transmission"})
else:
    car["transmission"] = "automatic"

car.pop("color")
keys = list(car.keys())


# key must be vaild data types, if it is a string it needs quotation marks

# .get gets us the item from the dictionary for us. and it gets rid of the error