#Super is used when child classs has its own init
class Food:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def calculate_price(self):
        print(f"The price is {self.price * self.quantity}")

class Burger(Food):
    def __init__(self, price, quantity, patty):
        super().__init__(price, quantity)
        self.patty = patty

    #Method overide calculate_price from children side will be called if both parent and child have same named function
    def calculate_price(self):
        print(f"The price is {(self.price * self.quantity)+(0.7 * self.patty)}")

class Pizza(Food):
    def __init__(self, price, quantity, topping):
        super().__init__(price, quantity)
        self.topping = topping

pizza = Pizza(10, 4, "halal bacon")

print(pizza.price)
print(pizza.quantity)
print(pizza.topping)

pizza.calculate_price()

burger = Burger(8, 6, 3)

print(burger.price)
print(burger.quantity)
print(burger.patty)

burger.calculate_price()
