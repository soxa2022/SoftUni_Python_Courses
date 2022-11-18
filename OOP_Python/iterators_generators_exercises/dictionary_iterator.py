class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == len(self.dictionary):
            raise StopIteration
        value_to_return = list(self.dictionary.items())[self.counter]
        self.counter += 1
        return value_to_return


# class dictionary_iter:
#
#     def __init__(self, dictionary: dict):
#         self.dictionary = list(dictionary.items())
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == len(self.dictionary):
#             raise StopIteration
#         value_to_return = self.dictionary[self.index]
#         self.index += 1
#         return value_to_return


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
