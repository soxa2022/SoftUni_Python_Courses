first_number = int(input())
second_number = int(input())
special_number = int(input())
for number in range(second_number, first_number - 1, -1):
    if number % 2 == 0:
        if number % 3 == 0:
            if number == special_number:
                break
            print(f"{number}", end=' ')
