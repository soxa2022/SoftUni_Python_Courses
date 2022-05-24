numbers = int(input())
percent_1 = 0
percent_2 = 0
percent_3 = 0
percent_4 = 0
percent_5 = 0
for i in range (1, numbers + 1):
    current_number = int(input())
    if current_number < 200:
        percent_1 += 1
    elif 200 <= current_number < 400:
        percent_2 += 1
    elif 400 <= current_number < 600:
        percent_3 += 1
    elif 600 <= current_number < 800:
        percent_4 += 1
    elif current_number >= 800:
        percent_5 += 1
percent_1 = (percent_1 / numbers) * 100
percent_2 = (percent_2 / numbers) * 100
percent_3 = (percent_3 / numbers) * 100
percent_4 = (percent_4 / numbers) * 100
percent_5 = (percent_5 / numbers) * 100
print(f"{percent_1:.2f}%")
print(f"{percent_2:.2f}%")
print(f"{percent_3:.2f}%")
print(f"{percent_4:.2f}%")
print(f"{percent_5:.2f}%")
