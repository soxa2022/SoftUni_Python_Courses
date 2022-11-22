from functools import wraps


def even_numbers(function):
    @wraps(function)
    def wrapper(*args):
        result = function(*args)
        return [x for x in result if x % 2 == 0]

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
