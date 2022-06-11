# def func_factorial(num_1, num_2):
#     fact_num_1 = 1
#     fact_num_2 = 1
#     for i in range(num_1, 0, -1):
#         fact_num_1 *= i
#     for k in range(num_2, 0, -1):
#         fact_num_2 *= k
#     return fact_num_1 / fact_num_2
#
#
# first_number = int(input())
# second_number = int(input())
# print(f"{func_factorial(first_number, second_number):.2f}")


def calculate_factorial(number):
    for factorial in range(1, number):
        number *= factorial
    return number


first_number = int(input())
second_number = int(input())
result = calculate_factorial(first_number) / calculate_factorial(second_number)
print(f"{result:.2f}")