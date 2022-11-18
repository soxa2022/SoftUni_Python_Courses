def solution():
    def integers():
        value = 1
        while True:
            yield value
            value += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for i in range(n):
            result.append(next(seq))
        return result
        # return [next(seq) for _ in range(n)]


    return take, halves, integers

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
