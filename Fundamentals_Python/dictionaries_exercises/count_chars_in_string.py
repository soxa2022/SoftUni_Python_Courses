strings = input()
dict_char = dict()
for char in strings:
    if char != " ":
        if char not in dict_char:
            dict_char[char] = 1
        else:
            dict_char[char] += 1
for key, val in dict_char.items():
    print(f"{key} -> {val}")

# strings = "".join(x for x in input().split())
# dict_char = {}
# for char in strings:
#     if char not in dict_char:
#         dict_char[char] = 0
#     dict_char[char] += 1
# for key, val in dict_char.items():
#     print(f"{key} -> {val}")
