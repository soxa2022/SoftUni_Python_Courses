def func_sorted(lst_number):
    lst_number = sorted(map(int, lst_number))
    return lst_number


# lst_numbers = [int(num) for num in input().split(" ")]
lst_numbers = input().split(" ")
print(func_sorted(lst_numbers))
