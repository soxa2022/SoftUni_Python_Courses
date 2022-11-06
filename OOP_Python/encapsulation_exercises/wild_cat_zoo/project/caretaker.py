from project.worker import Worker


class Caretaker(Worker):

    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age, salary)
