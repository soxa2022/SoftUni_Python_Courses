def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


NUMBERS = [int(x) for x in input().split()]
print(*selection_sort(NUMBERS))