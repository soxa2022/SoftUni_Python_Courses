import sys
from io import StringIO

test_input1 = '''5
01
. . . . .
. . . T .
. . . . .
. T . . .
. . F . .
down
right
right
right
down
right
up
down
right
up
End
'''
test_input2 = '''10
45
. . . . . . . . . .
. . T . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . F . . .
. . . . . . . . . .
. . . . . . . . . . 
. . . . . . . T . .
right
down
down
right
up
left
up
up
End
'''

# sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)


commands = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
racer_pos = [0, 0]
track = []
tunnels_pos = []
total_kilometers = 0
size = int(input())
racer_number = input()

for rows in range(size):
    line = input().split()
    if 'T' in line:
        tunnels_pos.append([rows, line.index("T")])
    track.append(line)

while True:
    direction = input()

    if direction == "End":
        track[racer_pos[0]][racer_pos[1]] = "C"
        print(f"Racing car {racer_number} DNF.")
        break

    racer_pos[0] = racer_pos[0] + commands[direction][0]
    racer_pos[1] = racer_pos[1] + commands[direction][1]

    if track[racer_pos[0]][racer_pos[1]] == "F":
        track[racer_pos[0]][racer_pos[1]] = "C"
        print(f"Racing car {racer_number} finished the stage!")
        total_kilometers += 10
        break

    elif track[racer_pos[0]][racer_pos[1]] == "T":
        track[racer_pos[0]][racer_pos[1]] = '.'
        tunnels_pos.remove([racer_pos[0], racer_pos[1]])
        racer_pos[0] = tunnels_pos[0][0]
        racer_pos[1] = tunnels_pos[0][1]
        track[racer_pos[0]][racer_pos[1]] = '.'
        total_kilometers += 30

    else:
        total_kilometers += 10


print(f"Distance covered {total_kilometers} km.")
[print(''.join(x)) for x in track]
