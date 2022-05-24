first_string = input()
second_string = input()
for char in range(len(first_string)):
    if first_string[char] != second_string[char]:
        first_string = first_string[:char] + second_string[char] + first_string[char + 1:]
        print(first_string)


# first_string = input()
# second_string = input()
# last_string = first_string
# for char in range(len(first_string)):
#     left_part = second_string[:char + 1]
#     right_part = first_string[char + 1:]
#     current_string = left_part + right_part
#     if current_string == last_string:
#         continue
#     print(current_string)
#     last_string = current_string
