from math import log2

from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    AVAILABLE_PROCESSORS = {"AMD Ryzen 7 5700G": 500, "Intel Core i5-12600K": 600, "Apple M1 Max": 1800}
    RAM_RANGE = [2 ** x for x in range(1, 8)]

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in DesktopComputer.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")
        if ram not in DesktopComputer.RAM_RANGE:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price += DesktopComputer.AVAILABLE_PROCESSORS[self.processor] + (int(log2(self.ram)) * 100)

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
