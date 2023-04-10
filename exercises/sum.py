"""Example function fo unit tests"""

def sum(xs: list[float]) ->float:
    "return sum of all elements in xs"
    sum_total: float = 0.0
    for idx in range(len(xs)): 
        sum_total += xs[idx] 
    return sum_total

print(sum( [1.0, -2.0, 1.0]))