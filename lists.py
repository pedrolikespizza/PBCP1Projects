# pb lists tuples and sets

# lists hold multiple pieces of info  

# to make a list you need brackets

# each item is seperated by a comma

# every item has to be a proper data type

# lists use index numbers alex is 0, katie is 1, andrew is 2, and so on.

# the * is the unpacking operator and it makes everything look clean

# adding a negative to the index makes the list go backward

# append adds to the end

# insert gets set to the index you want


# remove lets us remove the item

# pop puts two lists together based on the index. but if you don't put a index it removes the last index


#LISTS
siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]

for item in siblings: # for each item in siblings:
    if item==siblings[-1]: #if that item is equal to the last item in the list
        print("and "+item,end=".\n") #print "and Jake." instead of "Jake, "
    else: #else
        print(item,end=", ") #print "item, "

siblings.append("jayshree")
print(*siblings)




# tuples use parentheses

#tuples are i

#TUPLES
'''
subjects = ("CP1", "CP2", "Advanced CP", "CSP", "Utah Studies", "US 1" "US 2", "World Civ", "Geography", "CCA Business")
print(subjects[0])
print(*subjects)
subjects.append
'''



#SETS 
visited = {"Texas", "Ohio", "Minisoda", "Virgina", "D.C", "Utah", "California", "Nevada"}
print(*visited)
print(len(visited))
visited.add("Idaho")
print(*visited)
visited.update({"Montana", "Arazona", "Oklahoma", "New Mexico" })
print(*visited)
visited.remove("Arazona")
print(*visited)







#lists are ordered, mutable, and duplicates

#tuples are also ordered, immutable, and duplicates

#both lists and tuples can have duplicates 
#set are unordered, mutable, and does not allow duplicates