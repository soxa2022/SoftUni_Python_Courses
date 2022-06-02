n = int(input())
# lst_numbers = []
lst_numbers = [int(input()) for _ in range(n)]
filtered_list = []
command_even = "even"
command_odd = "odd"
command_pos = "positive"
command_neg = "negative"
# for _ in range(n):
#     number = int(input())
#     lst_numbers.append(number)
command = input()
for num in lst_numbers:
    filtered_command = ((command == command_even and num % 2 == 0) or (command == command_odd and num % 2 != 0) or
                        (command == command_pos and num >= 0) or (command == command_neg and num <= 0))
    if filtered_command:
        filtered_list.append(num)
print(filtered_list)
