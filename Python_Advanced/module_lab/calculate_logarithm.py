from math import log, e

number = int(input())
base_input = input()

if base_input.isnumeric():
    result = log(number, int(base_input))
else:
    result = log(number)

# base = e if base_input == 'natural' else int(base_input)
# result = log(number, base)
print(f'{result:.2f}')
