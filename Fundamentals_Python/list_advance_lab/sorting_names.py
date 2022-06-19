lst_names = input().split(", ")
new_list = sorted(lst_names, key=lambda x: (-len(x), str(x)))
print(new_list)
