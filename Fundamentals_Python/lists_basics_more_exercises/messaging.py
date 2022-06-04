# lst_number = list(input().split(" "))
lst_number = [number for number in input().split(" ")]
strings = input()
message = ''
for num in lst_number:
    sum_digits = 0
    for i in range(len(num)):
        sum_digits += int(num[i])
    idx = sum_digits
    if sum_digits >= len(strings):
        idx = sum_digits - len(strings)
    message += strings[idx]
    strings = strings[:idx] + strings[idx + 1:]
print(message)
