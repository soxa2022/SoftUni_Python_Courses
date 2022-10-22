def find_items_santa(rows, cols):
    item_list = ['D', 'C', 'G']
    items = 0
    santa_row = 0
    santa_col = 0
    for r in range(rows):
        for c in range(cols):
            if field[r][c] in item_list:
                items += 1
            if field[r][c] == 'Y':
                santa_row = r
                santa_col = c
    return santa_row, santa_col, items


count_rows, count_cols = [int(s) for s in input().split(', ')]
field = [[s for s in input().split()] for _ in range(count_rows)]
row, col, count_items = find_items_santa(count_rows, count_cols)
items_list = ['D', 'C', 'G']
found_items = []
is_collected = False
while True:
    if is_collected:
        print("Merry Christmas!")
        break
    command = input()
    if command == "End":
        break
    direct, step = command.split('-')
    for _ in range(int(step)):
        field[row][col] = 'x'
        if direct == "up":
            if row - 1 >= 0:
                row -= 1
            else:
                row = count_rows - 1
        elif direct == "down":
            if row + 1 < count_rows:
                row += 1
            else:
                row = 0
        elif direct == "right":
            if col + 1 < count_cols:
                col += 1
            else:
                col = 0
        elif direct == "left":
            if col - 1 >= 0:
                col -= 1
            else:
                col = count_cols - 1
        if field[row][col] in items_list:
            found_items.append(field[row][col])
        field[row][col] = 'Y'
        if len(found_items) == count_items:
            is_collected = True
            break
result = f"You've collected:\n- {found_items.count('D')} Christmas decorations\n- {found_items.count('G')} Gifts\n" \
         f"- {found_items.count('C')} Cookies"
print(result)
[print(*el) for el in field]