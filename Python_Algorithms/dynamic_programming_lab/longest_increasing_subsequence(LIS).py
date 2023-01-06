from collections import deque

nums = [int(x) for x in input().split()]

size = [0] * len(nums)
parent = [None] * len(nums)
best_size = 1
best_size_index = 0

size[0] = 1
for idx in range(1, len(nums)):
    current_number = nums[idx]
    current_best_size = 1
    current_parent = None

    for index in range(idx - 1, -1, -1):
        prev_num = nums[index]

        if prev_num >= current_number:
            continue

        if size[index] + 1 >= current_best_size:
            current_best_size = size[index] + 1
            current_parent = index

    size[idx] = current_best_size
    parent[idx] = current_parent
    if current_best_size > best_size:
        best_size = current_best_size
        best_size_index = idx

result = deque()

while best_size_index is not None:
    result.appendleft(nums[best_size_index])
    best_size_index = parent[best_size_index]
# print(best_size)
print(*result)