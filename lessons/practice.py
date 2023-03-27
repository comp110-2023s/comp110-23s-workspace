
b: list[int] = [2,4]

def g(x: list[int]) -> None:
    x[0] += 5
    
g(b)

print(b)



z: int = 5

def f(z: int) -> None:
    z += 2

f(z)
print(z)



c: dict[str, int] = {"a" : 1, "b": 2}

def h(x: dict[str, int]) -> None:
    x["a"] += 2

h(c)
print(c)