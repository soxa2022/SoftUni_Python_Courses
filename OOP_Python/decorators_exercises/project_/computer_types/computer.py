import abc
from math import log2, ceil, floor


class Computer(abc.ABC):
    AVAILABLE_PROCESSORS = {}

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == "":
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @staticmethod
    def power_of_two(n: int):
        result = log2(n)
        return floor(result) == ceil(result)

    @abc.abstractmethod
    def configure_computer(self, processor: str, ram: int):
        pass

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
