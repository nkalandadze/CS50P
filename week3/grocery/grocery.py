# დავალება #20 - Grocery List
from collections import Counter
grocery_list = []

# get a list of items from user
while True:
    try:
        item = input(f"").upper()
        grocery_list.append(item)
    except EOFError:
        break

# sort list alphabetically
grocery_list = sorted(grocery_list)

# create dictionary of items and their frequency in the list
list_dict = Counter(grocery_list)

# for each item print their frequency and name
for key in list(list_dict):
    print(f"{list_dict[key]} {key}")