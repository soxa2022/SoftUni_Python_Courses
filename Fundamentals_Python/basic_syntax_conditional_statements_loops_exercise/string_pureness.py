number_strings = int(input())
for char in range(number_strings):
    string = input()
    if "," in string or "." in string or "_" in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
# number_strings = int(input())
# for char in range(number_strings):
#     string = input()
#     if "," in string or "." in string or "_" in string:
#         print(f"{string} is not pure!")
#         continue
#     print(f"{string} is pure.")
