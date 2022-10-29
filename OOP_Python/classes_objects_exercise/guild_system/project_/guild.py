from player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."
        player.guild = self.name
        self.players.append(player)

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        kicked_player = [x for x in self.players if x.name == player_name]
        if not kicked_player:
            return f"Player {player_name} is not in the guild."
        # try:
        #     kicked_player = next(filter(lambda x: x.name == player_name, self.players))
        # except StopIteration:
        #     return f"Player {player_name} is not in the guild."
        kicked_player[0].guild = "Unaffiliated"
        self.players.remove(kicked_player)
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = [f"Guild: {self.name}"]
        for el in self.players:
            result.append(el.player_info())
        # [result.append(el.player_info()) for el in self.players]

        return '\n'.join(result)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
