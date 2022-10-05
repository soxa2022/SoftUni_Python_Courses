from io import StringIO
import sys

test_input = '''1
4
-5
3
10
'''
# sys.stdin = StringIO(test_input)


class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative()

