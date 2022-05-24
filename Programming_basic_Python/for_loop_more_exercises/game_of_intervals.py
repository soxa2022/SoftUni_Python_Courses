moves = int(input())
result = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
counter_6 = 0
for i in range(1, moves + 1):
    numbers = int(input())
    if 0 <= numbers < 10:
        result = result + 0.20 * numbers
        counter_1 = counter_1 + 1
    elif 10 <= numbers < 20:
        result += 0.30 * numbers
        counter_2 += 1
    elif 20 <= numbers < 30:
        result += 0.40 * numbers
        counter_3 += 1
    elif 30 <= numbers < 40:
        result += 50
        counter_4 += 1
    elif 40 <= numbers <= 50:
        result += 100
        counter_5 += 1
    elif numbers > 50 or numbers < 0:
        result = result / 2
        counter_6 += 1
print(f"{result:.2f}")
print(f"From 0 to 9: {(counter_1 / moves * 100):.2f}%")
print(f"From 10 to 19: {(counter_2 / moves * 100):.2f}%")
print(f"From 20 to 29: {(counter_3 / moves * 100):.2f}%")
print(f"From 30 to 39: {(counter_4 / moves * 100):.2f}%")
print(f"From 40 to 50: {(counter_5 / moves * 100):.2f}%")
print(f"Invalid numbers: {(counter_6 / moves * 100):.2f}%")

