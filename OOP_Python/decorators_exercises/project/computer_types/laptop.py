from math import log2

from project.computer_types.computer import Computer


class Laptop(Computer):
    AVAILABLE_PROCESSORS = {"AMD Ryzen 9 5950X": 900, "Intel Core i9-11900H": 1050, "Apple M1 Pro": 1200}
    RAM_RANGE = [2 ** x for x in range(1, 7)]

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in Laptop.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")
        if ram not in Laptop.RAM_RANGE:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        self.price += Laptop.AVAILABLE_PROCESSORS[self.processor] + (int(log2(self.ram)) * 100)

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
