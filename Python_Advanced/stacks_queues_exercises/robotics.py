from collections import deque


def calcul_time(start_time):
    hours, minutes, seconds = start_time.split(':')
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)


def converted_func(second):
    second %= 24 * 3600
    hour = second // 3600
    minute = (second - hour * 3600) // 60
    second = second - (hour * 3600 + minute * 60)
    return f"[{hour:02d}:{minute:02d}:{second:02d}]"


def robotic(robots_info, enter_time):
    time_seconds = calcul_time(enter_time)
    robots_info = [s.split("-") for s in robots_info]
    robots_data = {robots_info[i][0]: int(robots_info[i][1]) for i in range(0, len(robots_info))}
    available_robots = {robots_info[i][0]: 0 for i in range(0, len(robots_info))}
    line = deque()
    product = input()
    while not product == "End":
        line.append(product)
        product = input()
    while line:
        time_seconds += 1
        item = line.popleft()
        for name, next_time in available_robots.items():
            if next_time <= time_seconds:
                print(f"{name} - {item} {converted_func(time_seconds)}")
                available_robots[name] = time_seconds + robots_data[name]
                break
        else:
            line.append(item)


data = input().split(';')
input_time = input()
robotic(data, input_time)