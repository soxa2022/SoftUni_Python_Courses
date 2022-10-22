def bucket():
    points = 0
    for _ in range(3):
        row, col = [int(x) for x in input().strip('()').split(', ')]
        if 0 <= row < SIZE and 0 <= col < SIZE:
            if field[row][col] == "B":
                field[row][col] = 0
                points += sum(field[x][col] for x in range(SIZE))

    return points


SIZE = 6
field = [[x if x.isalpha() else int(x) for x in input().split()] for _ in range(SIZE)]

result = bucket()

if result < 100:
    print(f'Sorry! You need {100 - result} points more to win a prize.')
elif result < 200:
    print(f"Good job! You scored {result} points, and you've won Football.")
elif result < 300:
    print(f"Good job! You scored {result} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {result} points, and you've won Lego Construction Set.")
