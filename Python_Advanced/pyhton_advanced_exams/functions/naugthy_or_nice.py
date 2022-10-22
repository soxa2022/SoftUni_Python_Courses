def naughty_or_nice_list(kids: list, *args, **kwargs):
    sort_kids = {"Nice": [], "Naughty": [], "Not found": []}
    result = []
    if args:
        for s in args:
            s = s.split('-')
            if [x[0] for x in kids].count(int(s[0])) == 1:
                idx = [x[0] for x in kids].index(int(s[0]))
                sort_kids[s[1]].append(kids[idx][1])
                kids.pop(idx)
    if kwargs:
        for key, val in kwargs.items():
            if [x[1] for x in kids].count(key) == 1:
                sort_kids[val].append(key)
                idx = [x[1] for x in kids].index(key)
                kids.pop(idx)
    if kids:
        for _, name in kids:
            sort_kids["Not found"].append(name)
    for k,v in sort_kids.items():
        if v:
            result.append(f"{k}: {', '.join(v)}")
    return '\n'.join(result)

print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))



print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
