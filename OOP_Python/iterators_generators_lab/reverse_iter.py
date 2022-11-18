class reverse_iter:
    def __init__(self, numbers):
        self.numbers = list(numbers)
        self.index = len(numbers) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value_to_return = self.numbers[self.index]
        self.index -= 1
        return value_to_return

    # def __next__(self):
    #     if not self.numbers:
    #         raise StopIteration
    #
    #     return self.numbers.pop()

# class reverse_iter:
#     def __init__(self, numbers):
#         self.numbers = reversed(numbers)
#
#     def __iter__(self):
#         return iter(self.numbers)


reversed_list = reverse_iter([1, 2, 3, 4, 5])
for item in reversed_list:
    print(item)
# reversed_list = reverse_iter({1, 2, 3, 4, })
# for item in reversed_list:
#     print(item)
