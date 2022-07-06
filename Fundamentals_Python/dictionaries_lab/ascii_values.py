# dict_lst = {key: ord(key) for key in input().split(", ")}
lst = input().split(", ")
dict_lst = {key: ord(key) for key in lst}
print(dict_lst)

