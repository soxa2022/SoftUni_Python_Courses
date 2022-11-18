# class countdown_iterator:
#
#     def __init__(self, count: int):
#         self.count = count
#         self.counter = -count
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count + 1 == self.counter - 1:
#             raise StopIteration
#         value_to_return = self.count
#         self.count -= 1
#         self.counter += 1
#         return value_to_return


class countdown_iterator:

    def __init__(self, count: int):
        self.count = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration

        self.count -= 1

        return self.count

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
