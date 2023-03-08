"""Excersise 05: `list` Utility Functions"""

__author__ = "730575328"

def only_evens(og_list: list[int]):
    """Returns only the even numbers given a list."""
    evens: list[int] = []
    for i in og_list:
        if i % 2 == 0:
            evens.append(i)
    return print(evens)



