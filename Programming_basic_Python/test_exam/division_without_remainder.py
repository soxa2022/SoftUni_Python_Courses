count_numbers = int(input())
count_div_two = 0
count_div_three = 0
count_div_four = 0
for number in range(1, count_numbers + 1):
    num = int(input())
    if num % 2 == 0:
        count_div_two += 1
    if num % 3 == 0:
        count_div_three += 1
    if num % 4 == 0:
        count_div_four += 1
percent_div_two = count_div_two / count_numbers * 100
percent_div_three = count_div_three / count_numbers * 100
percent_div_four = count_div_four / count_numbers * 100
print(f"{percent_div_two:.2f}%")
print(f"{percent_div_three:.2f}%")
print(f"{percent_div_four:.2f}%")
