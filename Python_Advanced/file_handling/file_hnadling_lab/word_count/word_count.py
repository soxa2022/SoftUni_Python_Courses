import re


def get_words(file_path_words):
    with open(file_path_words, 'r') as file:
        words = (file.readline().split())
    return words


def count_words(file_path_text, words):
    words_dict = {}
    with open(file_path_text, 'r') as file:
        text = (file.readlines())
    for word in words:
        words_dict[word] = 0
        # words_dict[word] = len((re.findall(fr'\b{word}\b', text, re.IGNORECASE)))
        for line in text:
            # if word in line.lower():
            #     words_dict[word] += 1
            words_dict[word] += len((re.findall(fr'\b{word}\b', line, re.IGNORECASE)))
    return words_dict


def store_info(file_path_output, words_dict):
    result = ''
    for key, val in sorted(words_dict.items(), key=lambda x: -x[1]):
        result += f'{key} - {val}'
    with open(file_path_output, "w") as file:
        file.write(result)


file_path_words = 'words.txt'
file_path_text = "input.txt"
file_path_output = 'output.txt'

words = get_words(file_path_words)
counts = count_words(file_path_text, words)
store_info(file_path_output, counts)

# def read_words():
#     with open('./words_count_files/words.txt', 'r') as file:
#         return file.read().split(' ')
#
#
# def count_words_in_file(words):
#     words_counts = {
#         word: 0 for word in words
#     }
#
#     with open('./words_count_files/input.txt', 'r') as file:
#         for line in file:
#             words_in_line = [w.lower() for w in findall(r'\b\S+\b', line)]
#             for word in words:
#                 words_counts[word] += words_in_line.count(word.lower())
#     return words_counts
#
#
# words_counts = count_words_in_file(read_words())
# words_counts_sorted = sorted(words_counts.items(),
#                              key=lambda x: x[1],
#                              reverse=True)
# [
#     print(f'{w} - {c}') for w, c in words_counts_sorted
# ]
