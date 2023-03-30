""""Dictionary Function! - Ex07"""

__author__ = "730575328"

def invert(given:dict[str,str]) -> dict[str,str]:
    """Returns the inverted version of the given dictionary."""
    new_dict: dict[str,str] = {}
    for x in given:
        y = given[x]
        new_dict[y] = x
    return new_dict

def favorite_color(given:dict[str,str]) -> str:
    """Returns the favorite color that was repeated the most."""
    color: list[str] = []
    indx: int = 0
    temp = 0
    temp_color: str = ""
    new_dict: dict[str,str] = {}
    for x in given:
        y = given[x] 
        color.append(y)
    for i in color:
        for x in color:
            if x == i: indx += 1
        if indx > temp:
            temp = indx
            temp_color = i
    return temp_color

def count(list1: list[str]) -> dict[str, int]:
    """Takes a list and returns how many times each unique value was repeated in the list in a dictionary."""
    new_dict: dict[str,int] = {}
    for i in list1:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1
    return new_dict

print(count(["fish","shark","shark","orca","orca"]))