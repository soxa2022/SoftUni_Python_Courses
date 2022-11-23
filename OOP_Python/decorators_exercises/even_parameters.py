from functools import wraps


def even_parameters(function):
    @wraps(function)
    def wrapper(*args):
        if [x for x in args if not isinstance(x, int) or x % 2 != 0]:
            return "Please use only even numbers!"
        result = function(*args)
        return result

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
