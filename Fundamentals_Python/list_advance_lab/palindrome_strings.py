lst_words = [word for word in input().split(" ")]
palin_word = input()
lst_new_words = list()
for word in lst_words:
    if word == word[::-1]:
        lst_new_words.append(word)
print(lst_new_words, f"\nFound palindrome {lst_new_words.count(palin_word)} times")

# def palindrome_filter(word):
#     if word == word[::-1]:
#         return word
#
#
# words = input().split(" ")
# palindrome = input()
# palindrome_list = [word for word in words if palindrome_filter(word)]
# print(palindrome_list)
# print(f"Found palindrome {palindrome_list.count(palindrome)} times")
