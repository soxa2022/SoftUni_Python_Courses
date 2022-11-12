from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    EXPENSES = 200000
    AWARDS = [{1: 1000000, 3: 500000}, {5: 100000, 7: 50000}]

    def __init__(self, budget: int):
        super().__init__(budget)

    @property
    def sponsors_awards(self):
        return self.AWARDS

    @property
    def expenses(self):
        return self.EXPENSES
