from itertools import permutations

number = tuple(map(int, input()))
myperm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(number))
for digits in list(myperm):
    if digits > number:
        result = ''.join(str(x) for x in digits)
        print(result)
        break

# Създаване на set() от стринг и дублиращите елемнти се премахват.Така дължината на стринга е различна при повтарящите се цифри.
# year = int(input()) + 1
# while len(set(str(year))) != len(str(year)):
#     year += 1
# print(year)
