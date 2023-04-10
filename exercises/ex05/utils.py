"""Excersise 05: `list` Utility Functions!"""

__author__ = "730575328"


def only_evens(numbers: list[int]):
    """Returns only the even numbers given a list."""
    evens: list[int] = []
    for x in numbers:
        if x % 2 == 0:
            evens.append(x)
    return evens


def concat(list1: list[int], list2: list[int]):
    """Generates a new list that contains two combined lists."""
    new_list: list[int] = list1 + list2
    return new_list


def sub(list1: list[int], start: int, end: int): 
    """Generates a list that is a subset of the given list between the specificed start and end index."""
    sub_list: list[int] = []
    if start < 0:
        start = 0 
    if end > len(list1):
        end = len(list1)
    while start < end:
        sub_list.append(list1[start])
        start += 1
    return sub_list
