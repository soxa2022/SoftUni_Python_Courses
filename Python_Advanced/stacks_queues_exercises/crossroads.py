from collections import deque


def crossroads(green_time, window_time):
    time = green_time
    passed_cars = []
    cars = deque()
    data = input()
    while not data == "END":
        if not data == 'green':
            cars.append(data)
        else:
            green_time = time
            while cars:
                car = cars.popleft()
                if green_time > len(car):
                    passed_cars.append(car)
                    green_time -= len(car)
                elif green_time <= len(car):
                    if green_time + window_time >= len(car):
                        passed_cars.append(car)
                        break
                    else:
                        char = car[green_time + window_time]
                        print("A crash happened!")
                        print(f"{car} was hit at {char}.")
                        exit()
        data = input()
    else:
        print("Everyone is safe.")
        print(f"{len(passed_cars)} total cars passed the crossroads.")


green_light = int(input())
free_window = int(input())
crossroads(green_light, free_window)