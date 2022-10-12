def calc(sign, *args):
    if sign == '+':
        return f'{(args[0] + args[1]):.2f}'
    elif sign == '-':
        return f'{(args[0] - args[1]):.2f}'
    elif sign == '*':
        return f'{(args[0] * args[1]):.2f}'
    elif sign == '/':
        return f'{(args[0] / args[1]):.2f}'
    elif sign == '^':
        return f"{(args[0] ** args[1]):.2f}"
