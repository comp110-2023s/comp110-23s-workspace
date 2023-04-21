"""File to define Fish class!"""


class Fish:
    """This is my fish docstring!"""

    age: int = 0

    def __init__(self):
        """This is my fish docstring!"""
        self.age = 0
        return None
    
    def one_day(self) -> int:
        """This is my fish docstring!"""
        self.age += 1
        return self.age