"""If it's raining tell me to pack umbrella"""

weather: str = input("What is the weather like?: ")

if (weather == "rain"):
    print("Pack an umbrella")
elif (weather == "snow"):
    print("Bring a jacket")
else:
    print("The weather is good today")
    print("You don't need an umbrella")