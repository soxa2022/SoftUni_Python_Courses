# def smallest_number(x, y, z):
#     if x < y:
#         smallest_num = x
#     else:
#         smallest_num = y
#     if smallest_num < z:
#         return smallest_num
#     else:
#         return z

#
# def smallest_number_ver(x, y, z):
#     if x < y and x < z:
#         return x
#     elif y < x and y < z:
#         return y
#     else:
#         return z

def smallest_number(lst):
    return min(lst)


first_number = int(input())
second_number = int(input())
third_number = int(input())
all_numbers = [first_number, second_number, third_number]
print(smallest_number(all_numbers))
# print(smallest_number(first_number, second_number, third_number))
# print(smallest_number_ver(first_number, second_number, third_number))
