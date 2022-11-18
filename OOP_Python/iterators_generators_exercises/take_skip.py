class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.counter = 0
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.counter:
            raise StopIteration
        self.counter += 1
        value_to_return = self.value
        self.value += self.step
        return value_to_return

# class take_skip:
#
#     def __init__(self, step: int, count: int):
#         self.step = step
#         self.count = count
#         self.counter = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count -1 == self.counter :
#             raise StopIteration
#         self.counter += 1
#
#         return self.counter * self.step
