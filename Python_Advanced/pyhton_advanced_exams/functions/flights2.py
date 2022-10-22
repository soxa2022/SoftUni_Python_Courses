def flights(*args):
    info = {}
    for index in range(0, len(args), 2):
        if args[index] == "Finish":
            return info
        if args[index] in info:
            info[args[index]] += args[index + 1]
        else:
            info[args[index]] = args[index + 1]
    return info


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
