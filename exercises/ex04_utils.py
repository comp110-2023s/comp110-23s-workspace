"""Excersise 04: Lists - utility functions!"""

__author__ = "730575328"


def all(list: list[int], x: int) -> bool:
    """Indicates whether the integer given matches all the ones in the list."""
    i: int = 0
    if len(list) == 0:
        return False
    while i < len(list):
        if list[i] != x:
            return False
        else:
            i += 1
    return True


def max(list: list[int]) -> int:
    """Returns the largest number in the list."""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0 
    max_num: int = list[i]
    while i < len(list):
        if (list[i]) > max_num:
            max_num = list[i]
        i += 1
    return (max_num)


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns every element in two lists match at every index."""
    if len(list1) != len(list2):
        return False
    i: int = 0
    while i < len(list1):
        if list1[i] == list2[i]:
            i += 1
        else:
            return False
    return True