single_string = input()
list_animals = single_string.split(", ")
counter = len(list_animals)
for word in list_animals:
    counter -= 1
    if word == "wolf":
        if counter == 0:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")


# single_string = input()
# list_animals = single_string.split(", ")
# list_animals.reverse()
# for index, char in enumerate(list_animals):
#     if char == "wolf":
#         if index == 0:
#             print("Please go away and stop eating my sheep")
#         else:
#             print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")

