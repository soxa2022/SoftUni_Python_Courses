from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if price > self.__budget:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        try:
            worker = [x for x in self.workers if x.name == worker_name][0]
        except IndexError:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        sum_salaries = sum(x.salary for x in self.workers)
        if sum_salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= sum_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        sum_tended = sum(x.money_for_care for x in self.animals)
        if sum_tended > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= sum_tended
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]
        for item in ["Lion", "Tiger", "Cheetah"]:
            ll = [x for x in self.animals if x.__class__.__name__ == item]
            result.append(f"----- {len(ll)} {item}s:")
            [result.append(repr(x)) for x in ll]
        return "\n".join(result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]
        for item in ["Keeper", "Caretaker", "Vet"]:
            ll = [x for x in self.workers if x.__class__.__name__ == item]
            result.append(f"----- {len(ll)} {item}s:")
            [result.append(repr(x)) for x in ll]
        return "\n".join(result)
