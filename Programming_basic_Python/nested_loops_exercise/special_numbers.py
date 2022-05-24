number = int(input())
# counter_digits = 0
# for i in range(1111, 10000):
#     i = str(i)
#     counter_digits = 0
#     for index, digit in enumerate(i):
#         if int(digit) > 0 and number % int(digit) == 0:
#             counter_digits += 1
#         if counter_digits == 4:
#             counter_digits = 0
#             print(i, end=' ')
num = int(input())
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for m in range(1, 10):
                if num % i == 0 and num % j == 0 and num % k == 0 and num % m == 0:
                    print(f"{i}{j}{k}{m}", end=" ")

