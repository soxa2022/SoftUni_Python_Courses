data = input().upper()
symbols = ""
message = ''
numbers = ''
for idx, char in enumerate(data):
    if not char.isdigit():
        symbols += char
    else:
        numbers += char
        if idx <= len(data)-2:
            if data[idx+1].isdigit():
                continue
        message += symbols * int(numbers)
        symbols = ""
        numbers = ""
print(f"Unique symbols used: {len(set(message))}\n{message}")