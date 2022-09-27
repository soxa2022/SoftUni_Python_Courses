# def sorting_cheeses(**kwargs):
#     sorted_kwargs = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
#     result = ''
#     for name, quantities in sorted_kwargs:
#         result += name + '\n'
#         result += '\n'.join(([str(el) for el in sorted(quantities, reverse=True)])) + '\n'
#
#     return result
def sorting_cheeses(**kwargs):
    sorted_kwargs = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for name, quantities in sorted_kwargs:
        result.append(name)
        result.extend(sorted(quantities, reverse=True))

    return '\n'.join(([str(el) for el in result]))
