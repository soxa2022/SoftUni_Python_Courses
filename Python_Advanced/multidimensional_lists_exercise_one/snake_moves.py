import sys
from io import StringIO
from collections import deque

test_input1 = '''5 6
SoftUni
'''
test_input2 = '''1 4
Python
'''

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def snake_moves(rows, cols):
    matrix = [[None for _ in range(cols)] for _ in range(rows)]
    snake = deque(input())
    for row in range(rows):
        if row % 2 == 0:
            for col in range(cols):
                matrix[row][col] = snake[0]
                snake.append(snake.popleft())
        else:
            for col in range(-1, -cols - 1, -1):
                matrix[row][col] = snake[0]
                snake.append(snake.popleft())
    return matrix


count_rows, count_cols = [int(s) for s in input().split()]
[print(''.join(el)) for el in snake_moves(count_rows, count_cols)]

