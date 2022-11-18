# def fibonacci():
#     fib_result = [0, 1]
#     idx = 0
#     while True:
#         yield fib_result[idx]
#         number = fib_result[-1] + fib_result[-2]
#         fib_result.append(number)
#         idx += 1


def fibonacci():
    n1, n2 = 0, 1

    while True:
        yield n1
        n1, n2 = n2, (n1 + n2)
