# lst_strings = input().split()
# final_string = ''
# for word in lst_strings:
#     final_string += word*(len(word))
# print(final_string)
result = [word*len(word) for word in input().split()]
print("".join(result))
