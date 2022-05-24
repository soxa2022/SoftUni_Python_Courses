# count_numbers = int(input())
# is_even = True
# for number in range(count_numbers):
#     num = int(input())
#     if num % 2 != 0:
#         is_even = False
#         print(f"{num} is odd!")
#         break
# if is_even:
#     print("All numbers are even.")

count_numbers = int(input())
for number in range(count_numbers):
    num = int(input())
    if num % 2 != 0:
        print(f"{num} is odd!")
        break
else:
    print("All numbers are even.")
