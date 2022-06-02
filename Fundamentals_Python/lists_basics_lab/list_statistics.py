num = int(input())
lst_pos = []
lst_neg = []
for i in range(num):
    number = int(input())
    if number < 0:
        lst_neg.append(number)
    else:
        lst_pos.append(number)
print(lst_pos)
print(lst_neg)
print(f'Count of positives: {len(lst_pos)}\nSum of negatives: {sum(lst_neg)}')
# num = int(input())
# lst_pos = []
# lst_neg = []
# counter = 0
# sum_numbers = 0
# for i in range(num):
#     number = int(input())
#     if number < 0:
#         lst_neg.append(number)
#         sum_numbers += number
#     else:
#         lst_pos.append(number)
#         counter += 1
# print(lst_pos)
# print(lst_neg)
# print(f'Count of positives: {counter}')
# print(f"Sum of negatives: {sum_numbers}")

