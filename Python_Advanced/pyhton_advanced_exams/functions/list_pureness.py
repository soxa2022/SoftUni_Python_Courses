import sys
from collections import deque


def best_list_pureness(nums: list, k):
    nums = deque(nums)
    max_sum = - sys.maxsize
    pure_rotations = 0
    for x in range(k+1):

        current_sum = 0
        for i in range(len(nums)):
            current_sum += i * nums[i]
        if current_sum > max_sum:
            max_sum = current_sum
            pure_rotations = x

        nums.rotate(1)
    return f"Best pureness {max_sum} after {pure_rotations} rotations"


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
