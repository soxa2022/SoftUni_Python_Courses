# nums_stack = input().split()
#
# while nums_stack:
#     print(nums_stack.pop(), end=' ')

nums = input().split()
stack = []

while nums:
    stack.append(nums.pop())
print(" ".join(stack))