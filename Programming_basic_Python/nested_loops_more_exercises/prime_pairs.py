start_first_couple = int(input())
start_second_couple = int(input())
diff_first_couple = int(input())
diff_second_couple = int(input())
end_first_couple = start_first_couple + diff_first_couple
end_second_couple = start_second_couple + diff_second_couple
for i in range(start_first_couple, end_first_couple + 1):
    for j in range(2, i // 2):
        if (i % j) == 0:
            break
    else:
        for k in range(start_second_couple, end_second_couple + 1):
            for m in range(2, k // 2):
                if (k % m) == 0:
                    break
            else:
                print(f"{i}{k}")
            
