n = int(input())
s = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(97, 97 + s):
            for m in range(97, 97 + s):
                for p in range(1, n + 1):
                    if p > i and p > j:
                        print(f"{i}{j}{chr(k)}{chr(m)}{p}", end=' ')
