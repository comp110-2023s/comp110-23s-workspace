"""Excersise 05: `list` Utility Functions"""

__author__ = "730575328"

def only_evens(og_list: list[int]):
    """Returns only the even numbers given a list."""
    evens: list[int] = []
    for i in og_list:
        if i % 2 == 0:
            evens.append(i)
    return print(evens)

def concat(list1: list[int], list2: list[int]):
    """Generates a new list that contains two combined lists."""
    new_list: list[int] = list1 + list2
    return print(new_list)

def sub(list1: list[int], start: int, end: int): 
    """Generates a list that is a subset of the given list between the specificed start and end index."""
    sub_list: list[int] = []
    i = 0 
    while i < end:
        if i >= start:
            sub_list.append(list1[i])
            i += 1
        else:
            i += 1
    return(print(sub_list))