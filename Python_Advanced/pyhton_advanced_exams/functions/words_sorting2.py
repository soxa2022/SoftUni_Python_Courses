def words_sorting(*arg):
    words_dict = {}

    for word in arg:
        words_dict[word] = sum(ord(x) for x in word)

    if sum(words_dict.values()) % 2 != 0:
        result = []
        for key, val in sorted(words_dict.items(), key=lambda x: -x[1]):
            result.append(f"{key} - {val}")
    else:
        result = []
        for key, val in sorted(words_dict.items(), key=lambda x: x[0]):
            result.append(f"{key} - {val}")
    return '\n'.join(result)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))

print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
