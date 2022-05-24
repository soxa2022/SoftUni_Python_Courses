needed_height = int(input())
counter_failed_jumps = 0
counter_all_jumps = 0
start_height = needed_height - 30
is_failed = False
while start_height <= needed_height:
    jump_height = int(input())
    counter_all_jumps += 1
    if jump_height <= start_height:
        counter_failed_jumps += 1
        if counter_failed_jumps == 3:
            is_failed = True
            break
    else:
        start_height += 5
        counter_failed_jumps = 0
if is_failed:
    print(f"Tihomir failed at {start_height}cm after {counter_all_jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {needed_height}cm after {counter_all_jumps} jumps.")
    