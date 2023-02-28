"""EX04 - 'list' Utility Functions."""

__author__ = "730556365"


def all(int_list: list[int], int_checked: int) -> bool:
    """Checks if every index of a list is the same as an inputed integer."""
    idx: int = 0
    
    if len(int_list) == 0:
        return False

    while idx < len(int_list):
        if int_list[idx] != int_checked:
            return False
        idx += 1

    return True


def max(int_list: list[int]) -> int:
    """Finds the largest integer in a list."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")

    max_int: int = int_list[0]
    idx: int = 1

    while idx < len(int_list):
        if int_list[idx] > max_int:
            max_int = int_list[idx]
        idx += 1
    
    return max_int


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if two separate lists are of the same length and equal at each index."""
    idx: int = 0

    if len(list_1) != len(list_2):
        return False
    
    while idx < len(list_1):
        if list_1[idx] != list_2[idx]:
            return False
        idx += 1
    
    return True