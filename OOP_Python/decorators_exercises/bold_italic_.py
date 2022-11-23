from functools import wraps


def make_bold(function):
    @wraps(function)
    def wrapper(*args):
        result = function(*args)
        return "<b>" + result + "</b>"

    return wrapper


def make_italic(function):
    @wraps(function)
    def wrapper(*args):
        result = function(*args)
        return "<i>" + result + "</i>"

    return wrapper


def make_underline(function):
    @wraps(function)
    def wrapper(*args):
        result = function(*args)
        return f"<u>{result}</u>"

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
