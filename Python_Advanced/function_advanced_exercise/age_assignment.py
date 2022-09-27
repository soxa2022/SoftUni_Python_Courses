def age_assignment(*args, **kwargs):
    dd = {}
    ll = []
    for char, age in kwargs.items():
        for name in args:
            if name.startswith(char):
                dd[name] = age
    for key, val in sorted(dd.items()):
        ll.append(f"{key} is {val} years old.")
    return "\n".join(ll)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
