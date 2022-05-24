start_number = int(input())
end_number = int(input())
magic_number = int(input())
sum_numbers = 0
counter_numbers = 0
leave = False
for i in range(start_number, end_number + 1):
    for j in range(start_number, end_number + 1):
        sum_numbers = i + j
        counter_numbers = counter_numbers + 1
        if sum_numbers == magic_number:
            leave = True
            print(f"Combination N:{counter_numbers} ({i} + {j} = {magic_number})")
            break
    if leave:
        break
# if leave:
#     print(f"Combination N:{counter_numbers} ({i} + {j} = {magic_number})")
else:
    print(f"{counter_numbers} combinations - neither equals {magic_number}")