def print_stars_spaces(row, n):
    print((n - row) * " ", end='')
    print((row - 1) * '* ', end='')
    print("*")


def print_upper_part(n):
    for row in range(1, n + 1):
        print_stars_spaces(row, n)


def print_lower_part(n):
    for row in range(n - 1, 0, -1):
        print_stars_spaces(row, n)


def print_rhombus(n):
    print_upper_part(n)
    print_lower_part(n)


n = int(input())
print_rhombus(n)

# for row in range(1, n + 1):
#     print((n - row) * " ", end='')
#     print((row - 1) * '* ', end='')
#     print('*')
# for rows in range(n - 1, 0, -1):
#     print((n - rows) * " ", end='')
#     print((rows - 1) * '* ', end='')
#     print("*")
