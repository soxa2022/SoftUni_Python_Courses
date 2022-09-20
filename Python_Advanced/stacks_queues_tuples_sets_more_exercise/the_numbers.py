def add_numbers(seq, nums):
    seq.update(nums)
    return seq


def remove_numbers(seq, nums):
    seq = seq.difference(nums)
    return seq


def check_subset(first, second):
    x = (first.issubset(second), second.issubset(first))
    return any(x)


def numbers(first_s, second_s, num):
    for _ in range(num):
        command = input().split()
        if command[0] == "Add":
            input_nums = {int(s) for s in command if s.isdigit()}
            if command[1] == 'First':
                first_s = add_numbers(first_s, input_nums)
            elif command[1] == 'Second':
                second_s = add_numbers(second_s, input_nums)
        elif command[0] == 'Remove':
            input_nums = {int(s) for s in command if s.isdigit()}
            if command[1] == 'First':
                first_s = remove_numbers(first_s, input_nums)
            elif command[1] == 'Second':
                second_s = remove_numbers(second_s, input_nums)
        elif command[0] == 'Check':
            print(check_subset(first_s, second_s))
    print(*sorted(first_s), sep=', ')
    print(*sorted(second_s), sep=', ')


first_seq = set(int(s) for s in input().split())
second_seq = set(int(x) for x in input().split())
number = int(input())

numbers(first_seq, second_seq, number)

# def add_numbers(seq: list, nums):
#     seq = list(seq)
#     for num in nums:
#         seq.append(num)
#     return set(seq)
#
#
# def remove_numbers(seq, nums):
#     for num in nums:
#         seq.discard(num)
#     return seq
#
#
# def check_subset(first, second):
#     return first.issubset(second) or second.issubset(first)
#
#
# def numbers(first_s, second_s, num):
#     for _ in range(num):
#         command = input().split()
#         if command[0] == "Add":
#             stack = [int(s) for s in command if s.isdigit()]
#             if command[1] == 'First':
#                 first_s = add_numbers(first_s, stack)
#             elif command[1] == 'Second':
#                 second_s = add_numbers(second_s, stack)
#         elif command[0] == 'Remove':
#             stack = [int(s) for s in command if s.isdigit()]
#             if command[1] == 'First':
#                 first_s = remove_numbers(first_s, stack)
#             elif command[1] == 'Second':
#                 second_s = remove_numbers(second_s, stack)
#         elif command[0] == 'Check':
#             print(check_subset(first_s, second_s))
#     print(*sorted(first_s), sep=", ")
#     print(*sorted(second_s), sep=', ')
#
#
# first_seq = set(int(x) for x in input().split())
# second_seq = set(int(x) for x in input().split())
# number = int(input())
#
# numbers(first_seq, second_seq, number)
