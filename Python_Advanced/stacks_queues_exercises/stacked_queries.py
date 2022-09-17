def stacked(nums):
    stack = []
    for _ in range(nums):
        query = input().split()
        action = query[0]
        if action == '1':
            stack.append(query[1])
        elif action == '2':
            if stack:
                stack.pop()
        elif action == '3':
            if stack:
                print(max(stack))
        elif action == '4':
            if stack:
                print(min(stack))
    print(", ".join([stack.pop() for _ in range(len(stack))]))


number = int(input())
stacked(number)
