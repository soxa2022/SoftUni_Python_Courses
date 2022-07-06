# n = int(input())
# dict_syn = {}
# for i in range(n):
#     word = input()
#     synonym = input().split()
#     if word in dict_syn:
#         dict_syn[word] += synonym
#     else:
#         dict_syn[word] = synonym
# for word in dict_syn:
#     print(f"{word} - {', '.join(dict_syn[word])}")

# n = int(input())
# dict_syn = {}
# for i in range(n):
#     word = input()
#     synonym = input()
#     if word not in dict_syn:
#         dict_syn[word] = []
#     dict_syn[word].append(synonym)
# for word in dict_syn:
#     print(f"{word} - {', '.join(dict_syn[word])}")

from collections import defaultdict

synonyms = defaultdict(list)
number = int(input())

for _ in range(number):
    word, synonym = input(), input()
    synonyms[word].append(synonym)

data = [f"{word} - {', '.join(synonym)}" for word, synonym in synonyms.items()]
print('\n'.join(data))