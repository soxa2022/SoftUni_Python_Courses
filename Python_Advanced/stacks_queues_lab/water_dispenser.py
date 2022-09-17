from collections import deque


def water_dispenser(liters):
    line = deque()
    while True:
        name = input()
        if name == "Start":
            break
        line.append(name)
    command = input()
    while not command == "End":
        # if not command.startswith('refill'):
        if command.isdigit():
            needed_water = int(command)
            if liters >= needed_water:
                print(f"{line.popleft()} got water")
                liters -= needed_water
            else:
                print(f'{line.popleft()} must wait')
        else:
            _, add_litters = command.split()
            liters += int(add_litters)
        command = input()

    print(f"{liters} liters left")


water = int(input())
water_dispenser(water)
