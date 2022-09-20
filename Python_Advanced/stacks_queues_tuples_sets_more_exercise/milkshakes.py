# from collections import deque
#
#
# def milkshakes(choco_seq, milk_seq):
#     milkshake = 0
#     while choco_seq and milk_seq:
#         milk_cup = milk_seq.popleft()
#         choco_cup = choco_seq.pop()
#         if choco_cup <=0 and milk_cup <= 0:
#             continue
#         if choco_cup <= 0:
#             milk_seq.appendleft(milk_cup)
#             continue
#         if milk_cup <= 0:
#             choco_seq.append(choco_cup)
#             continue
#         if choco_cup == milk_cup:
#             milkshake += 1
#         else:
#             milk_seq.append(milk_cup)
#             choco_seq.append(choco_cup - 5)
#         if milkshake == 5:
#             print("Great! You made all the chocolate milkshakes needed!")
#             break
#     if milkshake != 5:
#         print("Not enough milkshakes.")
#     if choco_seq:
#         print(f'Chocolate: {", ".join(str(s) for s in choco_seq)}')
#     else:
#         print("Chocolate: empty")
#     if milk_seq:
#         print(f'Milk: {", ".join(str(s) for s in milk_seq)}')
#     else:
#         print("Milk: empty")
#
#
# chocolate_sequence = [int(s) for s in input().split(", ")]
# milk_sequence = deque([int(x) for x in input().split(', ')])
# milkshakes(chocolate_sequence, milk_sequence)


from collections import deque


def milkshakes(choco_seq, milk_seq):
    milkshake = 0
    while choco_seq and milk_seq and not milkshake == 5:
        milk_cup = milk_seq.popleft()
        choco_cup = choco_seq.pop()

        if choco_cup <= 0 and milk_cup <= 0:
            continue
        if choco_cup <= 0:
            milk_seq.appendleft(milk_cup)
            continue
        if milk_cup <= 0:
            choco_seq.append(choco_cup)
            continue
        if choco_cup == milk_cup:
            milkshake += 1
        else:
            milk_seq.append(milk_cup)
            choco_seq.append(choco_cup - 5)
    if not milkshake == 5:
        print("Not enough milkshakes.")
    else:
        print("Great! You made all the chocolate milkshakes needed!")
    if choco_seq:
        print(f'Chocolate: {", ".join(str(s) for s in choco_seq)}')
    else:
        print("Chocolate: empty")
    if milk_seq:
        print(f'Milk: {", ".join(str(s) for s in milk_seq)}')
    else:
        print("Milk: empty")


chocolate_sequence = [int(s) for s in input().split(", ")]
milk_sequence = deque([int(x) for x in input().split(', ')])
milkshakes(chocolate_sequence, milk_sequence)