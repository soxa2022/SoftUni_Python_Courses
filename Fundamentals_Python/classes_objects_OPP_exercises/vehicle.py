class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if self.owner is not None:
            return "Car already sold"
        elif money < self.price:
            return "Sorry, not enough money"
        else:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {(money - self.price):.2f}"

    def sell(self):
        if self.owner is None:
            return "Vehicle has no owner"
        self.owner = None

    def __repr__(self):
        if self.owner is None:
            return f"{self.model} {self.type} is on sale: {self.price}"
        return f"{self.model} {self.type} is owned by: {self.owner}"
# class Vehicle:
#     def __init__(self, type, model, price, owner=None):
#         self.type = type
#         self.model = model
#         self.price = price
#         self.owner = owner
#
#     def buy(self, money: int, owner: str):
#         if money >= self.price and self.owner is None:
#             self.owner = owner
#             result = money - self.price
#             return f"Successfully bought a {self.type}. Change: {result:.2f}"
#         elif money < self.price:
#             return "Sorry, not enough money"
#         else:
#             return "Car already sold"
#
#     def sell(self):
#         if self.owner is not None:
#             self.owner = None
#         else:
#             return "Vehicle has no owner"
#
#     def __repr__(self):
#         if self.owner:
#             return f"{self.model} {self.type} is owned by: {self.owner}"
#         return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
