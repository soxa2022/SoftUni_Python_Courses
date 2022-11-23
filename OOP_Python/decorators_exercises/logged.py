from functools import wraps


def logged(function):
    @wraps(function)
    def wrapper(*args):
        result = function(*args)
        return f'you called {function.__name__}{args}\nit returned {result}'
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))

print(func(4, 4, 4))
