from Player.player import Player


class Repository:
    def __init__(self):
        self._data = []

    def add(self, player):
        self._data.append(player)

    def remove(self, player):
        self._data.remove(player)

    def strength_increase(self, player):
        """
        Function used to increase a player's strength
        :param player: The player
        :return: -
        To increase the strength, we have to create another Player with the same credentials, and increased strength, while deleting the initial one
        """
        player_id = player.id
        name = player.name
        strength = player.strength
        strength += 1
        self._data.remove(player)
        self._data.append(Player(player_id, name, strength))

    def compare(self, player_one, player_two):
        if player_one > player_two:
            return 1
        elif player_two > player_one:
            return 2

    def sort_players(self):
        self._data.sort(key=lambda player: player.strength, reverse=True)

    def get_all_players(self):
        return self._data[:]

    def get_number_of_players(self):
        return len(self._data)
