# def reverse_array(idx, arr):
#     if idx == len(arr) - 1:
#         return arr[idx]
#
#     reverse_array(idx + 1, arr)
#     print(arr[idx], end=" ")

def reverse_array(idx, arr):
    if idx == len(arr) // 2:
        return
    ll[idx], ll[-1 - idx] = ll[-1 - idx], ll[idx]
    return reverse_array(idx + 1, arr)


# def iter_func(ll):
#     for idx in range(len(ll) // 2):
#         ll[idx], ll[-1 - idx] = ll[-1 - idx], ll[idx]
#     return " ".join(ll)


ll = input().split()
reverse_array(0, ll)
print(*ll, sep=" ")
# print(iter_func(ll))