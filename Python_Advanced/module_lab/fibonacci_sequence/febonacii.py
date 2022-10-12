sequence = []


def create_sequence(n):
    while sequence:
        sequence.pop()
    sequence.append(0)
    sequence.append(1)
    for i in range(2, n):
        next_num = sequence[-1] + sequence[-2]

        sequence.append(next_num)
    return ' '.join(str(x) for x in sequence)


def locate_number(n):
    if n in sequence:
        pos = sequence.index(n)
        return f"The number - {n} is at index {pos}"
    return f"The number {n} is not in the sequence"
