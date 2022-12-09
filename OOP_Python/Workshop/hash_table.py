class HashMap:
    def __init__(self):
        self.__max_capacity = 4
        self.__keys = [None] * self.__max_capacity
        self.__values = [None] * self.__max_capacity

    def get(self, key, default=None):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            return default

    def add(self, key, value):
        self[key] = value

    def size(self):
        return len([el for el in self.__keys if el is not None])

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError(key)

    def __setitem__(self, key, value):
        if key in self.__keys:
            index = self.__keys.index(key)
            self.__values[index] = value
            return

        if self.__max_capacity == self.size():
            self.__resize()

        index = self.__calc_index(key)
        index = self.__free_index(index)

        self.__keys[index] = key
        self.__values[index] = value

    def __len__(self):
        return self.__max_capacity

    def __str__(self):
        key_value_pairs = []

        for i in range(len(self.__keys)):
            if self.__keys[i] is not None:
                key_value_pairs.append(f"{self.__keys[i]}: {self.__values[i]}")

        return "{" + ', '.join(key_value_pairs) + "}"

    def __calc_index(self, key):
        return sum([ord(char) for char in str(key)]) % self.__max_capacity

    def __free_index(self, index):
        if index == self.__max_capacity:
            index = 0

        if self.__keys[index] is None:
            return index

        return self.__free_index(index + 1)

    def __resize(self):
        self.__keys = self.__keys + [None] * self.__max_capacity
        self.__values = self.__values + [None] * self.__max_capacity
        self.__max_capacity *= 2
