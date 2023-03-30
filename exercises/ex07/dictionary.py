"""Dictionary Function - EX07!"""

__author__ = "730575328"


def invert(given: dict[str, str]) -> dict[str, str]:
    """Returns the inverted version of the given dictionary."""
    new_dict: dict[str, str] = {}

    for key, value in given.items():
        if value in new_dict:
            raise KeyError (f"{value} is already in new_dict!")
        else:
            new_dict[value] = key
    return new_dict


def favorite_color(given: dict[str, str]) -> str:
    """Returns the favorite color that was repeated the most."""
    color: list[str] = []
    indx: int = 0
    temp: int = 0
    temp_color: str = ""
    for x in given:
        y = given[x] 
        color.append(y)
    for i in color:
        for x in color:
            if x == i: 
                indx += 1
        if indx > temp:
            temp = indx
            temp_color = i
    return temp_color


def count(list1: list[str]) -> dict[str, int]:
    """Takes a list and returns how many times each unique value was repeated in the list in a dictionary."""
    new_dict: dict[str, int] = {}
    for i in list1:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1
    return new_dict

print(favorite_color({"max": "brown","matt": "green","julian": "brown", "jasper": "green"}))