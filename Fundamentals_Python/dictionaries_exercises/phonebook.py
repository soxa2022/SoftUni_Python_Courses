phone_cat = {}
while True:
    name_numbers = input()
    if name_numbers.isdigit():
        break
    key, val = name_numbers.split("-")
    phone_cat[key] = val
n = int(name_numbers)
for _ in range(n):
    names = input()
    if names in phone_cat:
        print(f"{names} -> {phone_cat[names]}")
    else:
        print(f"Contact {names} does not exist.")