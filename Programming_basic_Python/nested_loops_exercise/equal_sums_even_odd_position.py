number_one = int(input())
number_two = int(input())

for i in range(number_one, number_two + 1):
    number_text = str(i)
    sum_odd_pos = 0
    sum_even_pos = 0
    # for j, digit in enumerate(number_text):
    for j in range(0, len(number_text)):
        if j % 2 == 0:
            digit = int(number_text[j])
            sum_even_pos += digit
        elif j % 2 != 0:
            digit = int(number_text[j])
            sum_odd_pos += digit
    if sum_even_pos == sum_odd_pos:
        print(number_text, end=' ')
 