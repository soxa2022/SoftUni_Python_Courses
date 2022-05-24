# floors = int(input())
# rooms = int(input())
# for i in range(floors, 0, -1):
#     print()
#     for j in range(rooms):
#         if i == floors:
#             print(f"L{i}{j}", end=" ")
#         elif i % 2 != 0:
#             print(f"A{i}{j}", end=" ")
#         elif i % 2 == 0:
#             print(f"O{i}{j}", end=" ")

floors = int(input())
rooms = int(input())
letter = ''
for i in range(floors, 0, -1):
    for j in range(rooms):
        if i == floors:
            letter = "L"
        elif i % 2 != 0:
            letter = "A"
        elif i % 2 == 0:
            letter = "O"
        print(f"{letter}{i}{j}", end=" ")
    print()
