# lst_numbers = [int(num) for num in input().split(" ")]
lst_numbers = input().split(" ")
lst_numbers = list(map(int, lst_numbers))
print(f"The minimum number is {min(lst_numbers)}")
print(f"The maximum number is {max(lst_numbers)}")
print(f"The sum number is: {sum(lst_numbers)}")
