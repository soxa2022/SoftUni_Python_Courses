string_input = input()
final_string = ""
lst_digits = [digit for digit in string_input if digit.isdigit()]
lst_non_digits = [ch for ch in string_input if not ch.isdigit()]
lst_taken_digit = list()
lst_skipped_digit = list()
for idx, digit in enumerate(lst_digits):
    if idx % 2 == 0:
        lst_taken_digit.append(int(digit))
    else:
        lst_skipped_digit.append(int(digit))
the_string = ''.join(lst_non_digits)
for idx in range(len(lst_taken_digit)):
    taken_idx = lst_taken_digit[idx]
    skipped_idx = lst_skipped_digit[idx]
    if taken_idx == 0:
        final_string += ""
    else:
        final_string += the_string[:taken_idx]
        the_string = the_string[taken_idx:]
    if skipped_idx == 0:
        the_string = the_string
    else:
        the_string = the_string[skipped_idx:]
print(final_string)