men = int(input())
women = int(input())
count_tables = int(input())
counter_tables = 0
for i in range(1, men + 1):
    for j in range(1, women + 1):
        counter_tables += 1
        if counter_tables <= count_tables:
            print(f"({i} <-> {j})", end=' ')

