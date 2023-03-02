"""Sum function with for ... in range(...) loop """

def sum(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    sum_total: float = 0.0
    for num in range(0, len(xs)):
        sum_total += xs[num]
    return sum_total