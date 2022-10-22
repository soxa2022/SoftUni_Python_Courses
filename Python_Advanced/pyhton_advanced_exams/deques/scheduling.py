stack = [int(s) for s in input().split(', ')]
input_index = int(input())
number = stack[input_index]
total_cycles = 0
nums_dict = {}
for idx, el in enumerate(stack):
    nums_dict[idx] = el

for key, val in sorted(nums_dict.items(), key=lambda x: (x[1], x[0])):

    total_cycles += val
    if number == val and key == input_index:
        break

print(total_cycles)
