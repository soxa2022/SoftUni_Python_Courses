def fill_the_box(height, length, width, *args):
    number = 0
    box = height * length * width
    for el in args:
        if el == 'Finish':
            break
        number += el
    if box >= number:
        return f"There is free space in the box. You could put {box - number} more cubes."
    return f"No more free space! You have {number - box} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
