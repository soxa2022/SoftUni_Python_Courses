def naughty_or_nice_list(kids: list, *args, **kwargs):
    sort_kids = {"Nice": [], "Naughty": [], "Not found": []}
    for command in args:
        num, mood = command.split('-')

        for tuple_ in kids:
            if [str(x[0]) for x in kids].count(num) == 1 and tuple_[0] == int(num):
                sort_kids[mood].append(tuple_[1])
                kids.remove(tuple_)
    for key, val in kwargs.items():
        for tuple_ in kids:
            if [str(x[1]) for x in kids].count(key) == 1 and tuple_[1] == key:
                sort_kids[val].append(key)
                kids.remove(tuple_)
    if kids:
        for _, name in kids:
            sort_kids['Not found'].append(name)

    result = []
    for k, v in sort_kids.items():
        if v:
            result.append(f"{k}: {', '.join(v)}")

    return "\n".join(result)


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
