# people = int(input())
# capacity = int(input())
# count_course = 0
# while people != 0:
#     if people > capacity:
#         people -= capacity
#         count_course += 1
#     else:
#         people -= people
#         count_course += 1
# print(count_course)

from math import ceil
people = int(input())
capacity = int(input())
count_course = ceil(people / capacity)
print(count_course)

people = int(input())
capacity = int(input())
count_course = people // capacity
if people % capacity != 0:
    count_course += 1
print(count_course)
