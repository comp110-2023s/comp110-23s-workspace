"""File to define Fish class"""

class Fish:
    
    age: int = 0

    def __init__(self):
        self.age = 0
        return None
    
    def one_day(self) -> int:
        self.age += 1
        return self.age
    

