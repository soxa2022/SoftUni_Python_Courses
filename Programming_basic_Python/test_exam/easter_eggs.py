count_eggs = int(input())
counter_red = 0
counter_orange = 0
counter_blue = 0
counter_green = 0
max_eggs = 0
colour = ''
for i in range(1, count_eggs + 1):
    paint_colour = input()
    if paint_colour == "red":
        counter_red += 1
    elif paint_colour == "orange":
        counter_orange += 1
    elif paint_colour == "blue":
        counter_blue += 1
    elif paint_colour == "green":
        counter_green += 1
if counter_red > max_eggs:
    max_eggs = counter_red
    colour = "red"
if counter_green > max_eggs:
    max_eggs = counter_green
    colour = "green"
if counter_orange > max_eggs:
    max_eggs = counter_orange
    colour = "orange"
if counter_blue > max_eggs:
    max_eggs = counter_blue
    colour = "blue"
print(f"Red eggs: {counter_red}")
print(f"Orange eggs: {counter_orange}")
print(f"Blue eggs: {counter_blue}")
print(f"Green eggs: {counter_green}")
print(f"Max eggs: {max_eggs} -> {colour}")
