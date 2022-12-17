def merge_list(left, right):
    sorted_list = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            sorted_list.append(left[left_idx])
            left_idx += 1
        else:
            sorted_list.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        sorted_list.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        sorted_list.append(right[right_idx])
        right_idx += 1
    return sorted_list


def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid_index = len(nums) // 2
    left = nums[:mid_index]
    right = nums[mid_index:]
    return merge_list(merge_sort(left), merge_sort(right))


numbers = [int(s) for s in input().split()]

print(*merge_sort(numbers))
