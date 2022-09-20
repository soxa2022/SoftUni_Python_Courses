from collections import deque


def paint_colors(main_string):
    main_color = ["red", "yellow", "blue"]
    secondary_color = {"orange": ('red', 'yellow'), "purple": ('red', 'blue'), "green": ('yellow', 'blue')}
    found_colors = []
    while len(main_string) > 1:
        left = main_string.popleft()
        right = main_string.pop()
        color = left + right
        new_color = right + left
        if color in main_color or color in secondary_color:
            found_colors.append(color)
        elif new_color in main_color or new_color in secondary_color:
            found_colors.append(new_color)
        else:
            left = left[:-1]
            right = right[:-1]
            if left:
                main_string.insert(len(main_string) // 2, left)
            if right:
                main_string.insert(len(main_string) // 2, right)
    if main_string:
        color = main_string.pop()
        if color in main_color or color in secondary_color:
            found_colors.append(color)
    for color in found_colors:
        if color not in main_color:
            if secondary_color[color][0] not in found_colors or secondary_color[color][1] not in found_colors:
                found_colors.remove(color)

    return found_colors


input_line = deque(input().split())
print(paint_colors(input_line))

