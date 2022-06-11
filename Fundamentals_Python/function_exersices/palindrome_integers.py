def func_palindrome(list_pos_int):
    for number in list_pos_int:
        if number == number[::-1]:
            print(True)
        else:
            print(False)


lst_numbers = input().split(", ")
func_palindrome(lst_numbers)

