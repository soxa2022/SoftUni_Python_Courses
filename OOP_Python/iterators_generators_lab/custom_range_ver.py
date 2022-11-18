class custom_iter:
    def __init__(self, cr):
        self.cr = cr
        self.next_number = self.cr.start

    def __next__(self):
        if self.next_number > self.cr.end:
            raise StopIteration
        return_value = self.next_number
        self.next_number += 1
        return return_value


class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.next_number = start

    def __iter__(self):
        return custom_iter(self)


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
