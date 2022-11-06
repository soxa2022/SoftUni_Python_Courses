class Player:

    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        result = []
        mangling_names = {"_Player__name": "Player",
                          "_Player__sprint": "Sprint",
                          "_Player__dribble": "Dribble",
                          "_Player__passing": "Passing",
                          "_Player__shooting": "Shooting"}
        [result.append(f'{mangling_names[key]}: {val}') for key, val in self.__dict__.items()]
        return '\n'.join(result)

    # def __str__(self):
    #     return f"Player: {self.name}\n" \
    #             f"Sprint: {self.__sprint}\n" \
    #             f"Dribble: {self.__dribble}\n"\
    #             f"Passing: {self.__passing}\n"\
    #             f"Shooting: {self.__shooting}"
