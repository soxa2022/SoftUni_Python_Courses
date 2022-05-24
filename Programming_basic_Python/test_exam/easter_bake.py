from math import ceil
count_bakes = int(input())
total_sugar = 0
total_flour = 0
max_sugar = 0
max_flour = 0
for i in range(1, count_bakes + 1):
    sugar_grams = int(input())
    flour_grams = int(input())
    total_sugar += sugar_grams
    total_flour += flour_grams
    if sugar_grams > max_sugar:
        max_sugar = sugar_grams
    if flour_grams > max_flour:
        max_flour = flour_grams
sugar_packages = ceil(total_sugar / 950)
flour_packages = ceil(total_flour / 750)
print(f"Sugar: {sugar_packages}")
print(f"Flour: {flour_packages}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
