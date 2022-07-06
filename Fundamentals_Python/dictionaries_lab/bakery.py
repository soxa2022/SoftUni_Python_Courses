elements = input().split(" ")
# bakery = {}
# for i in range(len(elements)):
#     if i % 2 == 0:
#         bakery[elements[i]] = int(elements[i+1])
# for i in range(0, len(elements), 2):
#     key = elements[i]
#     value = int(elements[i + 1])
#     bakery[key] = value
bakery = {elements[i]: int(elements[i + 1]) for i in range(0, len(elements), 2)}
print(bakery)
