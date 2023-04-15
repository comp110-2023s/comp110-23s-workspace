class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, num_added: float):
        new_point: Point = Point(self.x + num_added, self.y + num_added)
        return new_point
    


a: Point = Point(2.0, 4.0)

print(a)
print(a + 2.0)