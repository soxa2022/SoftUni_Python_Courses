from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSES = 250000
    AWARDS = [{1: 1500000, 2: 800000}, {8: 20000, 10: 10000}]

    def __init__(self, budget: int):
        super().__init__(budget)

    @property
    def sponsors_awards(self):
        return self.AWARDS

    @property
    def expenses(self):
        return self.EXPENSES
