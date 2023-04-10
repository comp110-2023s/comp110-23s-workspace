"""Define Pizza class"""

class Pizza: 

    #attributes
    size: str #small or large
    toppings: int 
    gluten_free: bool
    
    def __init__(self, size_input: str, toppings_input: int, gf_input: bool):
        self.size = size_input
        self.toppings = toppings_input
        self.gluten_free = gf_input
    
    def price(self) -> float:
        if self.size == "large":
            cost = 6.0
        else:
            cost = 5.0
        cost += .75 * self.toppings
        if self.gluten_free:
            cost += 1
        return cost



    

# returns self 