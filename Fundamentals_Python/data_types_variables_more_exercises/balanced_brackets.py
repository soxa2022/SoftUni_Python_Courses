number_lines = int(input())
count_open = 0
count_close = 0
is_valid = True
for i in range(number_lines):
    input_line = input()
    if input_line == "(":
        count_open += 1
    elif input_line == ")":
        count_close += 1
    if abs(count_close - count_open) > 1:
        is_valid = False
        break
if count_close == count_open and is_valid:
    print("BALANCED")
else:
    print("UNBALANCED")

