start_number = int(input())
end_number = int(input())

for i in range(start_number, end_number + 1):
    for j in range(start_number, end_number + 1):
        for k in range(start_number, end_number + 1):
            for m in range(start_number, end_number + 1):
                if i % 2 == 0 and m % 2 != 0 and i > m and (j + k) % 2 == 0:
                    print(f"{i}{j}{k}{m}", end=' ')
                if i > m and (j + k) % 2 == 0 and i % 2 != 0 and m % 2 == 0:
                    print(f"{i}{j}{k}{m}", end=' ')
