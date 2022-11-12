from project.animals.birds import Owl, Hen
from project.animals.mammals import Mouse
from project.food import Meat, Vegetable, Fruit

owl = Owl("Pip", 10, 10)
m = Mouse("P", 1, "Asia")
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)


hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(m.feed(meat))
m.feed(veg)
print(hen)
print(m)
