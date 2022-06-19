# lst_words = [word for word in input().split(" ") if len(word) % 2 == 0]
# for word in lst_words:
#     print(word)


words = input().split(" ")
lst_words = [word for word in words if len(word) % 2 == 0]
print("\n".join(lst_words))
# print(*lst_words, sep="\n")


# print("\n".join([word for word in input().split(" ") if len(word) % 2 == 0]))
