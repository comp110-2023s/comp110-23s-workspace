""""Practice with dictionaries"""

ice_cream: dict[str,int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

#Adding
ice_cream["mint"] = 3
print("After adding mint:")
print(ice_cream)

#removing
ice_cream.pop("mint")
print("After removing mint")
print(ice_cream)

#accessing
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

#updating a value
ice_cream["vanilla"] += 1
print(ice_cream)
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

#checking if in dictionary
print("mint" in ice_cream)
print("chocolate" in ice_cream)

