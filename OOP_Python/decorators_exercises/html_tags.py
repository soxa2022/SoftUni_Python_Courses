from functools import wraps


def tags(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            return f"<{n}>{result}</{n}>"

        return wrapper

    return decorator
