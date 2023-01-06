# Pascal triangle

def bin_coef(n, k, cache):
    if n == 0 or k == 0 or k == n:
        return 1
    key = (n, k)
    if key in cache:
        return cache[key]
    result = bin_coef(n - 1, k - 1, cache) + bin_coef(n - 1, k, cache)
    cache[key] = result
    return result


n = int(input())
k = int(input())

print(bin_coef(n, k, {}))
