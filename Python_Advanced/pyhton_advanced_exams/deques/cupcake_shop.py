def stock_availability(boxes: list, action, *args):
    if action == 'delivery':
        for item in args:
            boxes.append(item)
    elif action == 'sell':
        if not args:
            if boxes:
                boxes.pop(0)
        elif isinstance(args[0], int):
            boxes = boxes[args[0]:]
        else:
            for item in args:
                boxes = [s for s in boxes if s != item]
    return boxes
