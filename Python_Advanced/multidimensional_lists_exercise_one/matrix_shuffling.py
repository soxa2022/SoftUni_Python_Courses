import sys
from io import StringIO

test_input1 = '''2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END
'''
test_input2 = '''1 2
Hello World
0 0 0 1
swap 0 0 0 1
swap 0 1 0 0
END
'''

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

rows, cols = [int(s) for s in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([el for el in input().split()])
while True:
    command = input().split()
    if command[0] == "END":
        break
    if len(command) == 5:
        action, row1, col1, row2, col2 = [int(x) if x.isdigit() else x for x in command]
        if 0 <= row1 < rows and 0 <= row2 < rows and 0 <= col1 < cols and 0 <= col2 < cols:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(*el) for el in matrix]
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
