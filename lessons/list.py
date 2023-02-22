"""Practice with lists."""

grocery_lists: list[str] = list()
grocery_lists.append("bananas")
grocery_lists.append("milk")
grocery_lists.append("bread")
grocery_lists[1] = "cereal"
grocery_lists.pop(2)
print(grocery_lists)
print(grocery_lists[3])
