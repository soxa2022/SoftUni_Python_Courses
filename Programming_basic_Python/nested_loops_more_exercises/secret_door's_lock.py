first_num = int(input())
second_num = int(input())
third_num = int(input())
for i in range(1, first_num + 1):
    if second_num > 1:
        for k in range(2, second_num + 1):
            if k == 2 or k == 3 or k == 5 or k == 7:
                for j in range(1, third_num + 1):
                    if i % 2 == 0 and j % 2 == 0:
                        print(f"{i} {k} {j}")

