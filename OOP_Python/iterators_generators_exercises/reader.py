def read_next(*args):
    for seq in args:
        for el in seq:
            yield el
