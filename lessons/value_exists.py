"""Practice for test!"""

__author__ = "730575328"

def value_exists(arg_1: dict[str,int], arg_2: int) -> bool:
    for char in arg_1:
        if arg_1[char] == arg_2:
            return True
    return False
