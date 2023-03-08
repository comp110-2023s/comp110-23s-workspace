"""EX05 - `list` Utility Functions."""

__author__ = "730556365"

def only_evens(int_list: list[int]) -> list[int] :
    """Returns a list of only the even integers from the original list."""
    new_list: list[int] = list()
    for num in int_list:
        if num % 2 == 0:
            new_list.append(num)

    return new_list



def concat(list_one: list[int], list_two: list[int]) -> list[int] :
    """Returns a list where the the second list inputed is added on to the end of the first list inputed."""
    new_list: list[int] = list()
    for num in list_one:
        new_list.append(num)
    
    for num in list_two:
        new_list.append(num)

    return new_list



def sub(int_list: list[int], start_idx: int, end_idx: int) -> list[int] :
    """Returns a list cut out of the original list based on the interval of indexes given."""
    new_list: list[int] = list()
    if len(int_list) == 0 or start_idx >= len(int_list) or end_idx <= 0:
        return new_list
    if start_idx < 0:
        start_idx = 0
    if end_idx > len(int_list):
        end_idx = len(int_list)
   
    for num in range(start_idx, end_idx):
        new_list.append(int_list[num])

    return new_list