"""Practice for test!"""

__author__ = "730575328"

def odd_and_even(argument: list[int]) -> list[int]:
    " return a new list containing the elements of the input list that are odd and have an even index."
    new_list: list[int] = []
    i: int = 0
    for num in argument:
        if num % 2 != 0:
            if argument[i] == num:
                if i % 2 == 0: 
                    new_list.append(num)
        i += 1        
    return new_list

print(odd_and_even ([7 , 8 , 10 , 10 , 5 , 12 , 3 , 2 , 11 , 8]))
print (odd_and_even ([2 ,3 ,4 ,5]))