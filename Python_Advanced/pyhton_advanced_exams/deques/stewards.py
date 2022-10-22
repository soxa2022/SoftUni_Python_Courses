from collections import deque

seats = input().split(', ')
first_seq = deque(int(s) for s in input().split(', '))
second_seq = deque([int(x) for x in input().split(', ')])
taken_seats = []
rotations = 0
while rotations < 10 and len(taken_seats) < 3:
    first_num = first_seq.popleft()
    second_num = second_seq.pop()
    letter = chr(first_num + second_num)
    first_num_seat = str(first_num) + letter
    second_num_seat = str(second_num) + letter
    if first_num_seat in seats:
        if first_num_seat not in taken_seats:
            taken_seats.append(first_num_seat)
    elif second_num_seat in seats:
        if second_num_seat not in taken_seats:
            taken_seats.append(second_num_seat)
    else:
        first_seq.append(first_num)
        second_seq.appendleft(second_num)
    rotations += 1

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")