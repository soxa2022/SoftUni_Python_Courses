n = int(input())
counter = 1
is_bigger = False
for row in range(1, n + 1):
    for column in range(1, row + 1):
        print(counter, end=' ')
        counter += 1
        if counter > n:
            is_bigger = True
            break
    if is_bigger:
        break
    print()