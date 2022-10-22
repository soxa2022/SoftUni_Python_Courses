def numbers_searching(*args):
    duplicate_values = []
    values = []
    missing_value = None
    for num in args:
        if num not in values:
            values.append(num)
        else:
            duplicate_values.append(num)
    for number in range(min(values), max(values) + 1):
        if number not in values:
            missing_value = number

    result = [missing_value, sorted(set(duplicate_values))]
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))