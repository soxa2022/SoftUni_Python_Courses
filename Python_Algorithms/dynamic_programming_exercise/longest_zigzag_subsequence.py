from collections import deque

nums = [int(x) for x in input().split()]

dp = []
[dp.append([0] * len(nums)) for _ in range(2)]
parents = []
[parents.append([None] * len(nums)) for _ in range(2)]

best_size = 1
best_col_index = best_row_index = 0

dp[0][0] = 1
dp[1][0] = 1

for idx in range(1, len(nums)):
    current_number = nums[idx]

    for prev in range(idx - 1, -1, -1):
        prev_num = nums[prev]

        if prev_num < current_number and dp[0][prev] + 1 >= dp[1][idx]:
            dp[1][idx] = dp[0][prev] + 1
            parents[1][idx] = prev
        if prev_num > current_number and dp[1][prev] + 1 >= dp[0][idx]:
            dp[0][idx] = dp[1][prev] + 1
            parents[0][idx] = prev

    if best_size < dp[1][idx]:
        best_size = dp[1][idx]
        best_col_index = idx
        best_row_index = 1
    if best_size < dp[0][idx]:
        best_size = dp[0][idx]
        best_col_index = idx
        best_row_index = 0

result = deque()

while best_col_index is not None:
    result.appendleft(nums[best_col_index])
    best_col_index = parents[best_row_index][best_col_index]
    best_row_index = 1 if best_row_index == 0 else 0

print(*result)
