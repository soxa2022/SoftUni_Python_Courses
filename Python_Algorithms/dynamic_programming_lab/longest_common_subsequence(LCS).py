first_seq = input()
second_seq = input()

rows = len(first_seq) + 1
cols = len(second_seq) + 1

dp = []
[dp.append([0] * cols) for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if first_seq[row - 1] == second_seq[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

print(dp[rows - 1][cols - 1])

result = []
row = rows - 1
col = cols - 1

while row > 0 and col > 0:
    if first_seq[row - 1] == second_seq[col - 1]:
        result.append(first_seq[row - 1])  # second_seq[col-1]
        row -= 1
        col -= 1
    elif dp[row][col - 1] > dp[row - 1][col]:
        col -= 1
    else:
        row -= 1
# print(result[::-1])