# rooms = int(input())
# free_chairs = 0
# is_needed_chairs = True
# for room in range(1, rooms + 1):
#     strings = input().split(" ")
#     count_chairs = 0
#     if len(strings[0]) < int(strings[-1]):
#         count_chairs = int(strings[-1]) - len(strings[0])
#         print(f"{count_chairs} more chairs needed in room {room}")
#         is_needed_chairs = False
#     else:
#         free_chairs += len(strings[0]) - int(strings[-1])
# if is_needed_chairs:
#     print(f"Game On, {free_chairs} free chairs left")


def check_chairs(rooms):
    total_free_chairs = 0
    needed_chairs = 0
    for number_of_room in range(1, rooms + 1):
        free_chairs, visitors = input().split()
        difference = len(free_chairs) - int(visitors)
        if difference >= 0:
            total_free_chairs += difference
        else:
            needed_chairs += abs(difference)
            print(f"{abs(difference)} more chairs needed in room {number_of_room}")
    return total_free_chairs, needed_chairs


numbers_of_rooms = int(input())
total_free_chairs, needed_chairs = check_chairs(numbers_of_rooms)
if total_free_chairs >= needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
