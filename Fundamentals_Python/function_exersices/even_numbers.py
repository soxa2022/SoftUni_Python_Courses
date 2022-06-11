def even_number(lst_numbers):
    new_list = list(filter(lambda x: (x % 2 == 0), lst_numbers))
    return new_list


lst_nums = input().split(" ")
lst_nums = map(int, lst_nums)
# lst_nums = [int(n) for n in input().split(" ")]
print(even_number(lst_nums))

# def even_number(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
#
# lst_nums = [int(n) for n in input().split(" ")]
# lst_nums = list(filter(even_number, lst_nums))
# print(lst_nums)
