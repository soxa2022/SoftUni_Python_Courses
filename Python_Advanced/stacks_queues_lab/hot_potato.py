# from collections import deque
#
#
# def hot_potato(kids, tosses):
#     while len(kids) > 1:
#         kids.rotate(-tosses)
#         print(f"Removed {kids.pop()}")
#     print(f"Last is {kids.pop()}")
#
#
# queue = deque(input().split())
# num = int(input())
# hot_potato(queue, num)


from collections import deque


def hot_potato(kids, tosses):
    while len(kids) > 1:
        for idx in range(1, tosses + 1):
            if idx % tosses == 0:
                print(f"Removed {kids.popleft()}")
                break
            kids.append(kids.popleft())
    print(f"Last is {kids.pop()}")


queue = deque(input().split())
num = int(input())
hot_potato(queue, num)
