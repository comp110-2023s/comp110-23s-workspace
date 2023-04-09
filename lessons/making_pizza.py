"""Practice instantiating Pizza class"""

from pizza import Pizza

my_pizza: Pizza = Pizza("large",1, True	) # type: ignore
sals_pizza: Pizza = Pizza("small", 2, False)

# def price(pizza_order: Pizza):
#     if pizza_order.size == "large":
#         cost = 6.0
#     else:
#         cost = 5.0
#     cost += .75 * pizza_order.toppings
#     if pizza_order.gluten_free:
#         cost += 1
#     return cost

print(print(my_pizza))