# number = int(input())
# word = input()
# lst_words = []
# filter_list = []
# for i in range(number):
#     text = input()
#     lst_words.append(text)
# for j in range(len(lst_words)):
#     if word in lst_words[j]:
#         filter_list.append(lst_words[j])
# print(lst_words)
# print(filter_list)
number = int(input())
word = input()
lst_words = []
for i in range(number):
    text = input()
    lst_words.append(text)
print(lst_words)
for j in range(len(lst_words) - 1, -1, -1):
    if word not in lst_words[j]:
        lst_words.remove(lst_words[j])
print(lst_words)

