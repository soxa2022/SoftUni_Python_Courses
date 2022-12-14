# def sum_array(nums):
#     index = len(nums) - 1
#
#     if index == 0:
#         return nums[index]
#
#     return nums[index] + sum_array(nums[:-1])


def sum_array(nums, index):
    if index == len(nums) - 1:
        return nums[index]

    return nums[index] + sum_array(nums, index + 1)


print(sum_array([int(x) for x in input().split()], 0))
