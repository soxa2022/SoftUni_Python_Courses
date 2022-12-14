def fib(n):
    if n < 2:
        return 1

    return fib(n - 1) + fib(n - 2)


def fib_iter(n):
    result = 0
    fib1 = 0
    fib2 = 1
    for num in range(n):
        result = fib1 + fib2
        fib1, fib2 = fib2, result
    return result


# print(fib(int(input())))
print(fib_iter(int(input())))
