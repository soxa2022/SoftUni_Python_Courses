class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.next_number = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_number > self.end:
            raise StopIteration
        return_value = self.next_number
        self.next_number += 1
        return return_value


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
