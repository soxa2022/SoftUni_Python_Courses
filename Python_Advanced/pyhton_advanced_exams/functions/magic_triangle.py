def get_magic_triangle(n: int):
    triangle = [[1]]
    for i in range(2, n + 1):
        nums = [1]
        for j in range(1, i - 1):
            nums.append(triangle[-1][j - 1] + triangle[-1][j])
        nums.append(1)
        triangle.append(nums)
    return triangle


get_magic_triangle(5)

# from math import factorial
#
#
# def get_magic_triangle(n: int):
#     ll = []
#     for i in range(n):
#         a = []
#         for j in range(i + 1):
#             a.append(factorial(i) // (factorial(j) * factorial(i - j)))
#         ll.append(a)
#     return ll