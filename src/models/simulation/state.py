class State:
    def __init__(self):
        self.customers = 0
        self.groundCoffeeStock = 0

    def increaseCustomers(self):
        self.customers += 1

    def decreaseCustomers(self):
        self.customers = max(0, self.customers - 1)

    def increaseGroundCoffeeStock(self, amount):
        self.groundCoffeeStock += amount

    def decreaseGroundCoffeeStock(self, amount):
        self.groundCoffeeStock = max(0, self.groundCoffeeStock - amount)

    def __str__(self):
        return f"State(customers={self.customers}, groundCoffeeStock={self.groundCoffeeStock})"
