from print_line import printing_line

number = int(input())
for i in range(1, number + 1):
    printing_line(i)

for i in range(number - 1, 0, -1):
    printing_line(i)

