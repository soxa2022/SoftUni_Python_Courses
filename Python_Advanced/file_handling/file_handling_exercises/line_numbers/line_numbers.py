from string import punctuation


def line_numbers(path_input, path_output):
    result = []

    with open(path_input, 'r') as file:
        text = file.read().split('\n')

    with open(path_output, 'w') as file:

        for i in range(len(text)):
            letter_count = len([s for s in list(text[i]) if s.isalpha()])
            punctuation_count = len([s for s in list(text[i]) if s in punctuation])
            result.append(f'Line {i + 1}: {text[i].strip()} ({letter_count})({punctuation_count})\n')
        file.writelines(result)


# def line_numbers(path_input, path_output):
#     result = []
#
#     with open(path_input, 'r') as file:
#         text = file.readlines()
#
#     with open(path_output, 'w') as file:
#
#         for i in range(len(text)):
#             letter_count = len([s for s in list(text[i].strip()) if s.isalpha()])
#             punctuation_count = len([s for s in list(text[i].strip()) if not (s.isalpha() or s == " ")])
#             result.append(f'Line {i + 1}: {text[i].strip()} ({letter_count})({punctuation_count})')
#         file.writelines('\n'.join(result))


file_path_input = './text.txt'
file_path_output = './output.txt'
line_numbers(file_path_input, file_path_output)
