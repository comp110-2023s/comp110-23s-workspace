"""Sum function with for ... in ... loop """

def sum(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    sum_total: float = 0.0
    for num in xs:
        sum_total += num
    return sum_total