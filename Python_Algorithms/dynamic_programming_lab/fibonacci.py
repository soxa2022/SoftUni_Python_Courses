def fib(n, cache):
    if n <= 2:
        return 1
    if n in cache:
        return cache[n]
    result = fib(n - 1, cache) + fib(n - 2, cache)
    cache[n] = result
    return result


n = int(input())

print(fib(n, {}))