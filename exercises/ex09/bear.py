"""File to define Bear class"""

class Bear:
    age: int = 0
    hunger_score: int = 0
    
    def __init__(self):
        self.age = 0 
        self.hunger_score = 0
        return None
    
    def one_day(self) -> int:
        self.age += 1
        self.hunger_score =- 1
        return self.age
    
    def eat(self, num_fish: int):
        self.hunger_score += num_fish

    
    