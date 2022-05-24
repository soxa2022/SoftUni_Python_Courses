number = int(input())
special_numbers = ''
for i in range(1, number):
    for j in range(1, number):
        for k in range(1, number):
            for m in range(1, number):
                if (i + j) == (m + k) and number % (i + j) == 0:
                    special_numbers = (str(i) + str(j) + str(k) + str(m))
                else:
                    continue
                if 1000 < int(special_numbers) < 10000:
                    print(f"{special_numbers}", end=' ')
