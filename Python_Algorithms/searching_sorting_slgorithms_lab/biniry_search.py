def binary_search(numbers, target):
    min_index = 0
    max_index = len(numbers) - 1
    while min_index <= max_index:
        mid_index = (min_index + max_index) // 2
        mid_el = numbers[mid_index]
        if mid_el == target:
            return mid_index
        if mid_el < target:
            min_index = mid_index + 1
        else:
            max_index = mid_index - 1
    return -1


nums = [int(x) for x in input().split()]
targ = int(input())
print(binary_search(nums, targ))
