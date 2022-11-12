from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    BUDGET_CONST = 1_000_000

    def __init__(self, budget: int):
        self.budget = budget

    @property
    @abstractmethod
    def sponsors_awards(self):
        pass

    @property
    @abstractmethod
    def expenses(self):
        ...

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < FormulaTeam.BUDGET_CONST:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        for sponsors in self.sponsors_awards:
            for pos, award in sponsors.items():
                if race_pos <= pos:
                    revenue += award
                    break
        revenue -= self.expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
