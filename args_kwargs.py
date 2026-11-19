# pb args kwargs notes

def hello(name, *args):
    print(args)
    for first in args:
        print(f"hello{first} {name}!")

hello(" tung tung", " alex", " katie", " tia", " treyson", " jake")

hello("kringle, kris")


def clean(data, decimals= 0, **kwargs):
    if not kwargs.get("data"):
        return "there is no data."
    if kwargs.get("type")== "str":
        return kwargs.get("data").strip().lower()
    elif kwargs.get("type") == "int":
        return int(kwargs.get("data"))
    elif kwargs.get("type") == "float":
        if kwargs.get("decimals"):
            decimals = kwargs.get("decimals")
        return round(float(kwargs.get("data")),decimals)
    elif kwargs.get("type") == "list":
        return str(f"{x}, " for x in kwargs["data"])
    elif kwargs("type") == "bool":
        return f"{kwargs["data"]}"
    

print(clean(type="float", data="3.1415", decimals=3))
print(clean(data="utah", type = "str"))
print(clean())
# kwargs build dihtionary when we run it we can accses pieces of info to get a part of a dihtionary