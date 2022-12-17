# def insertion_sort(nums):
#     for i in range(1, len(nums)):
#         for j in range(i, 0, -1):
#             if nums[j] < nums[j - 1]:
#                 nums[j], nums[j - 1] = nums[j - 1], nums[j]
#
#     return nums

# def insertion_sort(nums):
#     for i in range(1, len(nums)):
#         for j in range(i, 0, -1):
#             if nums[j] < nums[j - 1]:
#                 nums[j], nums[j - 1] = nums[j - 1], nums[j]
#             else:
#                 break
#
#     return nums
def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums


numbers = [int(x) for x in input().split()]
print(*insertion_sort(numbers))