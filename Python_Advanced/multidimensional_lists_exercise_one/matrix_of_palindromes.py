import sys
from io import StringIO
import string

test_input1 = '''4 6
'''
test_input2 = '''3 2
'''

# sys.stdin = StringIO(test_input1)


# sys.stdin = StringIO(test_input2)


# def create_palindrome(n, m):
#     for row in range(n):
#         element_list = []
#         for col in range(m):
#             element = string.ascii_lowercase[row] + string.ascii_lowercase[row + col] + string.ascii_lowercase[row]
#             element_list.append(element)
#         print(*element_list)
#
#
# rows, cols = [int(s) for s in input().split()]
# create_palindrome(rows, cols)


def create_palindrome(n, m):
    matrix = []
    for row in range(n):
        element_list = []
        for col in range(m):
            result = string.ascii_lowercase[row] + string.ascii_lowercase[row + col] + string.ascii_lowercase[row]
            element_list.append(result)
        matrix.append(element_list)
    return matrix


rows, cols = [int(s) for s in input().split()]
[print(*el) for el in create_palindrome(rows, cols)]