# pb period 2 shopping list manager project

shopping_list=["candy", "cheese"]
while True:
    action = input("what would you like to do? add, remove, view, or exit: ")
    if action == "add": 
        add_item=input("what item do you want to add: ")
        shopping_list.append(add_item)
    elif action == "remove":
        remove_item =input("what do you want to remove: ")
        try:
            shopping_list.remove(remove_item)
        except:
            print("that doesn't exist")
            continue
    elif action == "view": 
        print(*shopping_list)  
    elif action == "exit":
        break
