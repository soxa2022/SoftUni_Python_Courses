from collections import deque


def truck_tour(nums):
    fuel_left = 0
    points = deque()
    for pump in range(nums):
        data = input().split()
        amount = int(data[0])
        distance = int(data[1])
        if amount + fuel_left >= distance:
            points.append(pump)
            fuel_left = amount + fuel_left - distance
        else:
            points.clear()
            fuel_left = 0

    return points.popleft()


number_pumps = int(input())
print(truck_tour(number_pumps))
