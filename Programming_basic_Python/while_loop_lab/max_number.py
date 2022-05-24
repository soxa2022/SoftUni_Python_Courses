import sys

number = input()
max_num = - sys.maxsize
while number != "Stop":
    number = int(number)
    if number > max_num:
        max_num = number
    number = input()
print(max_num)