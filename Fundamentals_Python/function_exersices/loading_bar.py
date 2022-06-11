# def loading_bar(number):
#     load_bar = list()
#     for digit in range(number//10):
#         load_bar.append("%")
#     for num in range((100 - number) // 10):
#         load_bar.append(".")
#     if number == 100:
#         return "100% Complete!\n"f"[{''.join(load_bar)}]"
#     else:
#         return f"{number}% [{''.join(load_bar)}]\nStill loading..."
#
#
# current_number = int(input())
# print(loading_bar(current_number))

def loading_bar(number):
    load_bar = "[]"
    idx = number // 10
    for i in range(1, idx + 1):
        load_bar = load_bar[:i] + "%" + load_bar[i:]
    load_bar = load_bar[:idx+1] + (10 - idx)*"." + load_bar[idx+1:]
    if number == 100:
        return f"100% Complete!\n{load_bar}"
    else:
        return f"{number}% {load_bar}\nStill loading..."


current_number = int(input())
print(loading_bar(current_number))


