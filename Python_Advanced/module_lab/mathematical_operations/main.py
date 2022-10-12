from calculator import calc

first_num, sign, second_num = input().split()

print(calc(sign, float(first_num), float(second_num)))

