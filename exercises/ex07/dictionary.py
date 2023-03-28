"""EX07 - Dictionary Functions."""

__author__ = "730556365"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """Function swaps the keys and values of a dictionary."""
    inverted_dict: dict[str, str] = dict()

    for key in inp_dict:
        if inp_dict[key] in inverted_dict:
            raise KeyError("The inverted dict results in multiple of the same key") 
        inverted_dict[inp_dict[key]] = key
    
    return inverted_dict


def favorite_color(inp_dict: dict[str, str]) -> str:
    """Function returns the color that appears the most in the values of a dictionary."""
    color_list: list[str] = list()
    counter_dict: dict[str, int] = dict()
    most_common: str = ""
    highest_count: int = 0

    for key in inp_dict:
        color_list.append(inp_dict[key])
    
    for color in color_list:
        if color in counter_dict:
            counter_dict[color] += 1
        else:
            counter_dict[color] = 1
    
    for color in counter_dict:
        if counter_dict[color] > highest_count:
            highest_count = counter_dict[color]
            most_common = color

    return most_common


def count(inp_list: list[str]) -> dict[str, int]:
    """Function counts the instances of an item in a list."""
    counter_dict: dict[str, int] = dict()

    for item in inp_list:
        if item in counter_dict:
            counter_dict[item] += 1
        else:
            counter_dict[item] = 1

    return counter_dict