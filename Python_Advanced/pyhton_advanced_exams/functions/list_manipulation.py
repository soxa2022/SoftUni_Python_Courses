def list_manipulator(ll: list, action: str, direction: str, *args):
    if action == "remove":
        if direction == 'end':
            if args:
                ll = ll[:(len(ll) - args[0])]
                return ll
            else:
                ll.pop()
                return ll
        elif direction == 'beginning':
            if args:
                ll = ll[args[0]:]
                return ll
            else:
                ll.pop(0)
                return ll
    elif action == 'add':
        if direction == 'end':
            for el in args:
                ll.append(el)
            return ll
        elif direction == 'beginning':
            for el in args[::-1]:
                ll.insert(0, el)
            return ll


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
