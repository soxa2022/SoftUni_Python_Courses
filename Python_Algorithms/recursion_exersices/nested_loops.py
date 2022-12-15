def nested_loops(idx, ll):
    if idx == len(ll):
        print(' '.join(str(x) for x in ll))
        return
    for num in range(1, len(ll) + 1):
        ll[idx] = num
        nested_loops(idx + 1, ll)


n = int(input())
ll = [None] * n
nested_loops(0, ll)