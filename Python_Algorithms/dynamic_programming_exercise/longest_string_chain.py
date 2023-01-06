from collections import deque

strings = [x for x in input().split()]

size = [0] * len(strings)
prev = [None] * len(strings)
best_size = 1
best_size_index = 0

size[0] = 1
for idx in range(1, len(strings)):
    current_number = len(strings[idx])
    current_best_size = 1
    current_parent = None

    for index in range(idx - 1, -1, -1):
        prev_num = len(strings[index])

        if prev_num >= current_number:
            continue

        if size[index] + 1 >= current_best_size:
            current_best_size = size[index] + 1
            current_parent = index

    size[idx] = current_best_size
    prev[idx] = current_parent
    if current_best_size > best_size:
        best_size = current_best_size
        best_size_index = idx

result = deque()

while best_size_index is not None:
    result.appendleft(strings[best_size_index])
    best_size_index = prev[best_size_index]
# print(best_size)
print(*result)


# strings = list(input().split())
#
# size = [0] * len(strings)
# prev = [None] * len(strings)
# best_size = 1
# best_size_index = 0
#
# size[0] = 1
# for idx in range(1, len(strings)):
#     current_word = strings[idx]
#     current_size = 1
#     current_parent = None
#
#     for index in range(idx - 1, -1, -1):
#         prev_word = strings[index]
#
#         if len(prev_word) >= len(current_word):
#             continue
#
#         if size[index] + 1 >= current_size:
#             current_size = size[index] + 1
#             current_parent = index
#
#     size[idx] = current_size
#     prev[idx] = current_parent
#     if current_size > best_size:
#         best_size = current_size
#         best_size_index = idx
#
# result = deque()
# index = best_size_index
# while index is not None:
#     result.appendleft(strings[index])
#     index = prev[index]
# # print(best_size)
# print(*result)
