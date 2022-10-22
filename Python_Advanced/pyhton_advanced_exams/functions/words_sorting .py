def words_sorting(*args):
    words = {}
    result = ''
    for key in args:
        words[key] = 0
        for ch in key:
            words[key] += ord(ch)
    sum_values = sum(value for value in words.values())
    if sum_values % 2 == 0:
        for char, val in sorted(words.items(), key=lambda x: x[0]):
            result += f"{char} - {val}\n"
    else:
        for char, val in sorted(words.items(), key=lambda x: -x[1]):
            result += f"{char} - {val}\n"
    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
