# def genrange(start, end):
#     for x in range(start, end + 1):
#         yield x

def genrange(start, end):
    value = start
    while value < end + 1:
        yield value
        value += 1
