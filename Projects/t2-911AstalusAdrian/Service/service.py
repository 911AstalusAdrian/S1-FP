from Player.player import Player


class Service:
    def __init__(self, player_repository):
        self._repository = player_repository

    def add_player(self, player_id, name, strength):
        player_to_add = Player(player_id, name, strength)
        self._repository.add(player_to_add)

    def get_last_players(self, number_of_players):
        last_players = []
        players = self.list_players()
        for index in range(len(players)-1, len(players)-number_of_players-1, -1):
            last_players.append(players[index])
        return last_players

    def play_game(self, player_one, player_two):
        """
        Service function that simulates the match between two players
        :param player_one: The first player of the match
        :param player_two: The second player
        :return: 1 if the first player won, 2 if the second one won
        We compare the strengths of the two players
        The one with the bigger strength wins, getting a strength 'boost', while the other one is out of the competition
        """
        winning_player = self._repository.compare(player_one, player_two)
        if winning_player == 1:
            self._repository.remove(player_two)
            self._repository.strength_increase(player_one)
        elif winning_player == 2:
            self._repository.remove(player_one)
            self._repository.strength_increase(player_two)
        return winning_player

    def list_players(self):
        return self._repository.get_all_players()

    def sort_players(self):
        self._repository.sort_players()

    def number_of_players(self):
        return self._repository.get_number_of_players()