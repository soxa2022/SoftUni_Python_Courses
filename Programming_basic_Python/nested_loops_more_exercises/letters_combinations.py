start_letter = input()
end_letter = input()
pass_letter = input()
first_letter = ''
second_letter = ''
third_letter = ''
counter = 0
for i in range(ord(start_letter), ord(end_letter) + 1):
    if ord(pass_letter) == i:
        continue
    else:
        first_letter = chr(i)

    for j in range(ord(start_letter), ord(end_letter) + 1):
        if ord(pass_letter) == j:
            continue
        else:
            second_letter = chr(j)

        for k in range(ord(start_letter), ord(end_letter) + 1):
            if ord(pass_letter) == k:
                continue
            else:
                third_letter = chr(k)
                print(f"{first_letter}{second_letter}{third_letter}", end=' ')
                counter += 1
print(counter)
