"""Dictionary Function - EX07!"""

__author__ = "730575328"


def invert(given: dict[str, str]) -> dict[str, str]:
    """Returns the inverted version of the given dictionary."""
    new_dict: dict[str, str] = {}

    for key, value in given.items():
        if value in new_dict:
            raise KeyError(f"{value} is already in new_dict!")
        else:
            new_dict[value] = key
    return new_dict


def favorite_color(given: dict[str, str]) -> str:
    """Returns the favorite color that was repeated the most."""
    most_common: dict[str,int] = {}

    for name,color in given.items():
        if color not in most_common:
            most_common[color] = 1
        else: 
            most_common[color] = 1

    most_common_colors: str = ""
    most_common_count: int = 0 


    for color,count in most_common.items():
        if most_common[color] > most_common_count:
            most_common_color = color
            most_common_count = most_common[color]
    return most_common_color
     


def count(list1: list[str]) -> dict[str, int]:
    """Takes a list and returns how many times each unique value was repeated in the list in a dictionary."""
    new_dict: dict[str, int] = {}
    for i in list1:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1
    return new_dict