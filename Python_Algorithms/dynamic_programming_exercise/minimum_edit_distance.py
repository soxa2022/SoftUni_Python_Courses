replace = int(input())
insert = int(input())
delete = int(input())

str_1 = input()
str_2 = input()

rows = len(str_1) + 1
cols = len(str_2) + 1
dp = []
[dp.append([0] * cols) for _ in range(rows)]
dp[0][0] = 0

for row in range(1, rows):
    dp[row][0] = row * delete
for col in range(1, cols):
    dp[0][col] = col * insert

for row in range(1, rows):
    for col in range(1, cols):

        if str_1[row - 1] == str_2[col - 1]:
            dp[row][col] = dp[row - 1][col - 1]

        else:
            dp[row][col] = min(dp[row-1][col-1] + replace, dp[row - 1][col] + delete, dp[row][col - 1] + insert)

print(f"Minimum edit distance: {dp[rows - 1][cols - 1]}")