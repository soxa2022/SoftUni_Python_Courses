def tribonacci(n):
    i = 0
    list_numbers = [0, 0, 1]
    while n > i:
        print(list_numbers[-1], end=' ')
        tribo_number = sum(list_numbers)
        list_numbers.append(tribo_number)
        list_numbers.remove(list_numbers[0])
        i += 1


count_number = int(input())
tribonacci(count_number)
