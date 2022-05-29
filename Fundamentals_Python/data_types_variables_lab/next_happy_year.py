year = int(input())
next_happy_year = year + 1
while True:
    is_found = False
    next_happy_year = str(next_happy_year)
    for digit in next_happy_year:
        count = 0
        for num in next_happy_year:
            if num == digit:
                count += 1
            if count > 1:
                break
        if count > 1:
            break
    else:
        is_found = True
    if is_found:
        print(next_happy_year)
        break
    else:
        next_happy_year = int(next_happy_year)
        next_happy_year += 1

# Вариант 2 на колега
# input_year = int(input())
# next_year = input_year + 1
# next_happy_year = ""
# while True:
#     str_next_year = str(next_year)
#     for i in range(0, len(str_next_year)):
#         if str_next_year[i] not in next_happy_year:
#             next_happy_year = next_happy_year + str_next_year[i]
#     if len(next_happy_year) == len(str_next_year):
#         break
#     next_happy_year = ""
#     next_year += 1
# print(next_happy_year)


# Създаване на set() от стринг и дублиращите елемнти се премахват.Така дължината на стринга е различна при повтарящите се цифри.
# year = int(input()) + 1
# while len(set(str(year))) != len(str(year)):
#     year += 1
# print(year)
