def dup(xs: list[str]):
    start_len: int = len(xs)
    i: int = 0
    while i <= start_len - 1:
        xs.append(xs[1])
        i += 1

groceries: list[str] = ["apples", "eggs"]
print(dup(groceries))
print(groceries)