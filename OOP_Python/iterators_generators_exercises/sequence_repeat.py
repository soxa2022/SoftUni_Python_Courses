class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.idx = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter != self.number:
            if self.idx == len(self.sequence):
                self.idx = 0
            value_to_return = self.sequence[self.idx]
            self.idx += 1
            self.counter += 1
            return value_to_return
        else:
            raise StopIteration

# class sequence_repeat:
#     def __init__(self, sequence: str, number: int):
#         self.sequence = sequence
#         self.number = number
#         self.idx = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.idx == self.number - 1:
#             raise StopIteration
#
#         self.idx += 1
#
#         return self.sequence[self.idx % len(self.sequence)]

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
