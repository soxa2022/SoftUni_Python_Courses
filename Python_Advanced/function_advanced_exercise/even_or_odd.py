# def even_odd(*args):
#     if args[-1] == "even":
#         return [s for s in args[:-1] if s % 2 == 0]
#     elif args[-1] == "odd":
#         return [s for s in args[:-1] if not s % 2 == 0]

def even_odd(*args):
    *ll, command = args
    if command == "even":
        return [s for s in ll if s % 2 == 0]
    elif command == "odd":
        return [s for s in ll if not s % 2 == 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
