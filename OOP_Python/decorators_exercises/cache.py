from functools import wraps


# def cache(func):
#     logs = {}
#
#     @wraps(func)
#     def wrapper(n):
#         if n in logs:
#             return logs[n]
#         result = func(n)
#         logs[n] = result
#         return result
#
#     wrapper.log = logs
#     return wrapper
def cache(func):
    @wraps(func)
    def wrapper(n):
        if n not in wrapper.log:
            result = func(n)
            wrapper.log[n] = result
            return result

        return wrapper.log[n]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
fibonacci(4)
print(fibonacci.log)
