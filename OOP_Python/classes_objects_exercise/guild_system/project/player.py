class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return f"Skill already added"

    def player_info(self):
        result = ''
        result += f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"
        for skill_name, skill_mana_cost in self.skills.items():
            result += f"==={skill_name} - {skill_mana_cost}\n"
        return result
