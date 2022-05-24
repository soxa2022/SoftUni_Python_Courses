# import sys
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
# max_number = - sys.maxsize
# if first_number > max_number:
#     max_number = first_number
# if second_number > max_number:
#     max_number = second_number
# if third_number > max_number:
#     max_number = third_number
# print(max_number)


first_number = int(input())
second_number = int(input())
third_number = int(input())
if first_number > second_number and first_number > third_number:
    print(first_number)
elif second_number > first_number and second_number > third_number:
    print(second_number)
else:
    print(third_number)

# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
# print(max(first_number, second_number, third_number))
