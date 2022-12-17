def bubble_sort(nums):
    while True:
        swap_count = 0
        for curr_idx in range(len(nums) - 1):
            if nums[curr_idx] > nums[curr_idx + 1]:
                nums[curr_idx], nums[curr_idx + 1] = nums[curr_idx + 1], nums[curr_idx]
                swap_count += 1

        if swap_count == 0:
            return nums

# def bubble_sort(nums):
#     is_sorted = False
#     counter = 0
#     while not is_sorted:
#         is_sorted = True
#         for curr_idx in range(1, len(nums) - counter):
#             if nums[curr_idx - 1] > nums[curr_idx]:
#                 nums[curr_idx], nums[curr_idx - 1] = nums[curr_idx - 1], nums[curr_idx]
#                 is_sorted = False
#         counter += 1
#     return nums


#
# def bubble_sort(nums):
#     for i in range(len(nums)):
#         for j in range(1, len(nums) - i):
#             if nums[j - 1] > nums[j]:
#                 nums[j], nums[j - 1] = nums[j - 1], nums[j]
#     return nums


numbers = [int(s) for s in input().split()]

print(*bubble_sort(numbers))