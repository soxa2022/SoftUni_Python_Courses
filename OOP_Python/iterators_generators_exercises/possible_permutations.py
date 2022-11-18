from itertools import permutations


def possible_permutations(numbers):
    ll = permutations(numbers)
    for el in ll:
        yield list(el)

# def possible_permutations(numbers):
#     if len(numbers) == 0:
#         yield []
#     else:
#         for idx in range(len(numbers)):
#             current_result = numbers[:idx] + numbers[idx + 1:]
#             for p in possible_permutations(current_result):
#                 yield [numbers[idx]] + p


[print(n) for n in possible_permutations([1, 2, 3])]