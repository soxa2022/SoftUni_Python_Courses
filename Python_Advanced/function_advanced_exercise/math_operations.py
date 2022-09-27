def math_operations(*args, **kwargs):
    ll = []
    index = 0
    for key in kwargs:
        for i in range(index, len(args), 4):
            if key == 'a':
                kwargs[key] += args[i]
            elif key == 's':
                kwargs[key] -= args[i]
            elif key == 'd':
                if not args[i] == 0:
                    kwargs[key] /= args[i]
            elif key == 'm':
                kwargs[key] *= args[i]
        index += 1
    for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x)):
        ll.append(f"{key}: {value:.1f}")
    return '\n'.join(ll)



print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))

