x: int = 10
result: str = ""

while x>=0:
    if x % 3 > 0:
        result=result+str(x)
    else:
        result = str(x)+result
    x = x-1

print(result)