tail = input()
body = input()
head = input()
# list_meerkat = [head, body, tail]
list_meerkat = [tail, body, head]
# list_meerkat[0], list_meerkat[-1] = list_meerkat[-1], list_meerkat[0]
list_meerkat[0], list_meerkat[2] = list_meerkat[2], list_meerkat[0]
print(list_meerkat)