# lst_numbers = [float(num) for num in input().split(" ")]
# # lst_numbers = list(map(lambda x: abs(x), lst_numbers))
# # print(lst_numbers)
lst_numbers = input().split(" ")
new_list = list()
# new_list = []
for i in lst_numbers:
    number = abs(float(i))
    new_list.append(number)
print(new_list)