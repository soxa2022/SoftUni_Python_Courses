age = float(input())
sex = input()
if sex == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")
if sex == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")


