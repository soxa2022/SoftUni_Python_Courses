def fashion_func(clothes, rack):
    sum_clothes = 0
    rack_number = 1
    while clothes:
        if sum_clothes + clothes[-1] < rack:
            sum_clothes += clothes.pop()
        elif sum_clothes + clothes[-1] == rack:
            sum_clothes += clothes.pop()
            if clothes:
                rack_number += 1
            sum_clothes = 0
        else:
            sum_clothes = 0
            rack_number += 1
            sum_clothes += clothes.pop()
    return rack_number


box_with_clothes = [int(s) for s in input().split()]
capacity = int(input())
print(fashion_func(box_with_clothes, capacity))


