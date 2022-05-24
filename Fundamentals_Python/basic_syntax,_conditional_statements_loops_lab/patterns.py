# number = int(input())
# for col in range(1, number + 1):
#     for row in range(1, col):
#         print("*", end='')
#     print()
# for col in range(number + 1, 1, -1):
#     for row in range(col, 1, -1):
#         print("*", end='')
#     print()

number = int(input())
for i in range(1, number + 1):
    print(i * "*")
for j in range(number - 1, 0 , -1):
    print(j * "*")
