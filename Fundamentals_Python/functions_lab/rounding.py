# def convert_list(base_list):
#     new_list = list()
#     for i in base_list:
#         number = round(float(i))
#         new_list.append(number)
#     return new_list
#
#
# input_list = input().split(" ")
# print(convert_list(input_list))
# # lst_numbers = [float(num) for num in input().split(" ")]
lst_numbers = input().split(" ")
lst_numbers = map(float, lst_numbers)
print(list(map(lambda x: round(x), lst_numbers)))
