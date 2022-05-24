control_number = int(input())
counter_numbers = 0
save_pass = 0
is_pass = False
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if control_number == a * b + c * d:
                    if a < b and c > d:
                        print(f"{a}{b}{c}{d}", end=' ')
                        counter_numbers += 1
                        if counter_numbers == 4:
                            save_pass = f"{a}{b}{c}{d}"
                            is_pass = True
if is_pass:
    print()
    print(f"Password: {save_pass}")
else:
    print()
    print("No!")
