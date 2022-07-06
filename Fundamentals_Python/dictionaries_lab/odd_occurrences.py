words = input().split()
my_dict = {}
for word in words:
    key = word.lower()
    if key not in my_dict:
        my_dict[key] = 1
    else:
        my_dict[key] += 1
# for k in my_dict:
#     if my_dict[k] % 2:
#         print(k, end=' ')
# for k, v in my_dict.items():
#     if v % 2:
#         print(k, end=' ')
lst = dict(list(filter(lambda kvp: kvp[1] % 2, my_dict.items())))
print(" ".join(lst.keys()))
# for i in range(len(lst)):
#     print(lst[i][0], end=" ")

# words = input().split()
# my_dict = {}
# for word in words:
#     key = word.lower()
#     if key not in my_dict:
#         my_dict[key] = 1
#     else:
#         my_dict[key] += 1
# # for k in my_dict:
# #     if my_dict[k] % 2:
# #         print(k, end=' ')
# lst = list(filter(lambda kvp: kvp[1] % 2, my_dict.items()))
# for i in range(len(lst)):
#     print(lst[i][0], end=" ")
from collections import defaultdict

words = input().split(' ')
counter_of_words = defaultdict(int)

for word in words:
    counter_of_words[word.lower()] += 1

print(' '.join([word for word, count in counter_of_words.items() if count % 2 != 0]))