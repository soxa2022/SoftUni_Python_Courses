# def sum_numbers(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2, n3):
#     return sum_numbers(n1, n2) - n3
#
#
# def add_and_subtract(x, y, z):
#     sum_numbers(x, y)
#     return subtract(x, y, z)

def sum_numbers(n1, n2):
    return n1 + n2


def subtract(sums, n3):
    return sums - n3


def add_and_subtract(n1, n2, n3):
    result = subtract(sum_numbers(n1, n2), n3)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
