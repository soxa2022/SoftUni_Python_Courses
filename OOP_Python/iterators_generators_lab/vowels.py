class vowels:
    vowels = ["a", "e", "o", "u", "i", "y"]

    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index != len(self.string):
            value_to_return = self.string[self.index]
            self.index += 1
            if value_to_return.lower() in self.vowels:
                return value_to_return
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
