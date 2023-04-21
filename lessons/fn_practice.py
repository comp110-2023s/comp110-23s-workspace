""""Example functions to learn defintion and """


def my_max(number1: int, number2: int) -> int:
    """Returns the maxmium value out of two numbers"""
    if number1 >= number2:
        return number1 
    else: #number1 < number2
        return number2

max_number: int = my_max(1,10)
other_max_numnber: int = my_max(11,3)
print(other_max_numnber)

