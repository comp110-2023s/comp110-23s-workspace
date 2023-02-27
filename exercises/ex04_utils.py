"""EX04 - 'list' Utility Functions!"""

__author__ = "730558596"


def all(input: list[int], num: int) -> bool:
    """Returns true or false statement given the list and the num value."""
    count: int = 0
    yes: int = 0
    if len(input) == yes:
        return False
    while count < len(input):
        if input[count] != num:
            return False
        count = count + 1 
    return True


def max(input: list[int]) -> int:
    """Returns maximum value within the list, but will result in a error if there is a empty list!"""
    if len(input) == 0: 
        raise ValueError("max() arg is an empty List")
    maxint: int = input[0]
    count: int = 0
    while count < len(input):
        if maxint < input[count]: 
            maxint = input[count]
            count = count + 1
        else:
            count = count + 1
    return maxint


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Checks if two strings are matching. Returns true if they are the same list and if the function was given two empty strings. Returns false if the lists are not the same."""
    if len(input1) != len(input2):
        return False
    count: int = 0
    boolresult: bool = True 
    while count < len(input1) and len(input2):
        if input1[count] == input2[count]:
            boolresult
        else:
            return False
        count = count + 1 
    return boolresult
