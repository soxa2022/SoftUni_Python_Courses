rows = int(input())
ship_destroyed = 0
# matrix = list()
# for i in range(rows):
#     lst_numbers = [int(number) for number in input().split(" ")]
#     matrix.append(lst_numbers)
matrix = [[int(number) for number in input().split(" ")] for i in range(rows)]
number_attacks = input().split(" ")
for attack in number_attacks:
    attack = attack.split("-")
    row_idx = int(attack[0])
    col_idx = int(attack[1])
    if matrix[row_idx][col_idx] != 0:
        matrix[row_idx][col_idx] -= 1
        if matrix[row_idx][col_idx] == 0:
            ship_destroyed += 1
print(ship_destroyed)