def nums_battle(*args):
    def sum_negative():
        return sum([x for x in args if x < 0])

    def sum_positive():
        return sum([x for x in args if x > 0])

    if abs(sum_negative()) > abs(sum_positive()):
        return f'''{sum_negative()}
{sum_positive()}
The negatives are stronger than the positives'''
    return f'''{sum_negative()}
{sum_positive()}
The positives are stronger than the negatives'''


nums = [int(s) for s in input().split()]
print(nums_battle(*nums))
