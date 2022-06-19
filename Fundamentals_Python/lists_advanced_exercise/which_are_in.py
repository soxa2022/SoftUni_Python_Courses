lst_strings = input().split(", ")
lst_words = input().split(", ")
new_list = list()
for strings in lst_strings:
    for word in lst_words:
        if strings in word:
            new_list.append(strings)
            break
# new_list = [x for x in lst_strings if any(x in w for w in lst_words)]
print(new_list)
