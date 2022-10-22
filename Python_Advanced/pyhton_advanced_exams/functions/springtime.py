example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }


def start_spring(**kwargs):
    spring = {}
    result = []
    for key, val in kwargs.items():
        if val not in spring:
            spring[val] = []
        spring[val].append(key)
    for k, v in sorted(spring.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{k}:")
        for i in sorted(v):
            result.append(f'-{i}')
    return '\n'.join(result)


print(start_spring(**example_objects))
