"""Challenge Question 04 - Dict Function Writing"""

__author__ = "730556365"


def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    "Function returns a dictionary from a list of keys and a list of values"
    new_dict: dict[str, int] = dict()
    
    if len(keys) != len(values) or len(keys) == 0 or len(values) == 0:
        return new_dict
    
    for idx in range(0, len(keys)):
        new_dict[keys[idx]] = values[idx]

    return new_dict