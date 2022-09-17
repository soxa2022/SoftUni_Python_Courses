from collections import deque


def balanced_func(data):
    is_unbalanced = True
    second_data = data.copy()

    while data:
        if not len(data) % 2 == 0:
            is_unbalanced = False
            break
        if (data.popleft() + data.pop()) not in ['[]', '()', '{}'] and (second_data.popleft() + second_data.popleft()) not in ['[]', '()', '{}']:

            is_unbalanced = False
            break
    if is_unbalanced:
        return "YES"
    return 'NO'


queue = deque(input())
print(balanced_func(queue))

