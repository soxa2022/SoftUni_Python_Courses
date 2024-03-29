import sys
from io import StringIO
test_input0 = '''1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
'''

test_input1 = '''1, 4, 5
'''
test_input2 = '''4, 5, 6, 1, 3
'''
test_input3 = '''2, 5, 10
'''
# sys.stdin = StringIO(test_input0)
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)

numbers_list = [int(s) for s in input().split(", ")]
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif number <= 10:
        result /= number

print(result)
