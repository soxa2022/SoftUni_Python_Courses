first_cables = [int(x) for x in input().split()]
second_cables = [s for s in range(1, len(first_cables) + 1)]

rows = len(first_cables) + 1
cols = len(second_cables) + 1

dp = []
[dp.append([0] * cols) for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if first_cables[row - 1] == second_cables[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

print(f"Maximum pairs connected: {dp[rows - 1][cols - 1]}")

# first_cables = [int(x) for x in input().split()]
# size = len(first_cables) + 1
# second_cables = [s for s in range(1, size)]
#
# lcs = []
# [lcs.append([0] * size) for _ in range(size)]
#
# for row in range(1, size):
#     for col in range(1, size):
#         if first_cables[row - 1] == second_cables[col - 1]:
#             lcs[row][col] = lcs[row - 1][col - 1] + 1
#         else:
#             lcs[row][col] = max(lcs[row - 1][col], lcs[row][col - 1])
#
# print(f"Maximum pairs connected: {lcs[size - 1][size - 1]}")
