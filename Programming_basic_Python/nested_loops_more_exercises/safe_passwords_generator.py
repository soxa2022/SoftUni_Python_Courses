first_number = int(input())
second_number = int(input())
max_count_pass = int(input())
symbol_a = 35
symbol_b = 64
end_symbol_a = 55
end_symbol_b = 96
counter_pass = 0
is_max_pass = False
for k in range(1, first_number + 1):
    for m in range(1, second_number + 1):
        if counter_pass < max_count_pass:
            print(f"{chr(symbol_a)}{chr(symbol_b)}{k}{m}{chr(symbol_b)}{chr(symbol_a)}", end='|')
            symbol_a += 1
            symbol_b += 1
            counter_pass += 1
        else:
            is_max_pass = True
            break
        if symbol_a > 55:
            symbol_a = 35
        if symbol_b > 96:
            symbol_b = 64
        if is_max_pass:
            break
    if is_max_pass:
        break
