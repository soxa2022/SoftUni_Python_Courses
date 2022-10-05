def replace_symbols(symbol, path, sep):
    result = []

    with open(path, 'r') as file:
        text = file.readlines()
        even_lines = [text[i] for i in range(len(text)) if i % 2 == 0]
        for el in even_lines:
            for ch in symbol:
                if ch in el:
                    el = el.replace(ch, sep)
            result.append(el.split()[::-1])

    return result


file_path = './text.txt'
symbols = ["-", ",", ".", "!", "?"]
char = '@'
res = replace_symbols(symbols, file_path, char)
# [print(*x) for x in res]
print(*[' '.join(x) for x in res], sep="\n")
