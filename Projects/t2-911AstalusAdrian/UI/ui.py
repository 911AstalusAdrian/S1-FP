from Player.player import Player
import random


class UI:
    def __init__(self, player_service):
        self._service = player_service

    def run(self):
        self.get_players()
        self.sort()
        print("Hello and welcome to this year's UBB Tennis Championship!")
        player_number = self._service.number_of_players()
        print("We have " + str(player_number) + " players! ")
        print("Here are the players: \n")
        self.list_players()
        '''
        Based on the number of players, we decide which bracket will be played
        Before that, we have to play qualifiers to reduce the number of players
        We get the required number of players from the end of the list (players having the lowest strength)
        We simulate the games
        The remaining players will play the tournament in a similar way
        '''
        bracket = self.decide_bracket(player_number)
        print("\nWe'll play the round of " + str(bracket) + " but first, qualifiers: ")
        players_for_quali = (player_number - bracket) * 2
        if players_for_quali != 0:
            last_players = self._service.get_last_players(players_for_quali)
            self.play_qualifiers(last_players)
        print("\nThese are our remaining " + str(bracket) + " players")
        self.list_players()

        done = False
        while not done:
            player_count = self._service.number_of_players()
            player_list = self._service.list_players()
            print("\nLast " + str(player_count) + ": ")
            self.list_remaining_players(player_list)
            self.play_game(player_list)
            remaining_players = self._service.number_of_players()
            if remaining_players == 1:
                print("\nWe have a winner!")
                self.list_players()
                done = True
        print("\nWell, that was it! The games were insane, I hope you guys liked it")

    def play_game(self, player_list):
        """
        Function used to simulate the matches, using a copy of the actual list of players
        :param player_list: Copy of the list of players still remaining in the tournament
        :return: -
        Using random.choice we get a random player from the list
        After that, we remove it so we don't pick the same player twice
        We let the user take his/her guess
        Using the players, we simulate a game, which returns the winner
        Depending on the winner and the user input, we show different messages
        """
        while player_list:
            player_one = random.choice(player_list)
            player_list.remove(player_one)
            player_two = random.choice(player_list)
            player_list.remove(player_two)
            print("\n")
            print(player_one)
            print("  vs.  ")
            print(player_two)
            user_choice = int(input("Who wins? 1 or 2? "))
            winning_player = self._service.play_game(player_one, player_two)
            if winning_player == 1 and user_choice == 1:
                print(player_one.name + " won the game, +1 strength!")
            elif winning_player == 2 and user_choice == 2:
                print(player_two.name + " won the game, +1 strength!")
            else:
                print("You were close, but the other player won. +1 strength to him.")

    @staticmethod
    def list_remaining_players(players):
        for player in players:
            print(player)

    @staticmethod
    def decide_bracket(number_of_players):
        brackets = [2, 4, 6, 8, 16, 32]
        for index in range(len(brackets)):
            if number_of_players < 32 and brackets[index] < number_of_players < brackets[index + 1]:
                return brackets[index]
            elif number_of_players >= 32:
                return 32

    def play_qualifiers(self, player_list):
        while player_list:
            player_one = random.choice(player_list)
            player_list.remove(player_one)
            player_two = random.choice(player_list)
            player_list.remove(player_two)
            print("\n")
            print(player_one)
            print("  vs.  ")
            print(player_two)
            winning_player = self._service.play_game(player_one, player_two)
            if winning_player == 1:
                print(player_one.name + " won the game, +1 strength!")
            elif winning_player == 2:
                print(player_two.name + " won the game, +1 strength!")

    def get_players(self):
        file = open("players.txt", 'r+')
        for line in file:
            player_information = line.strip().split(",")
            player_id = int(player_information[0])
            player_name = player_information[1]
            player_strength = int(player_information[2])
            self._service.add_player(player_id, player_name, player_strength)
        file.close()

    def list_players(self):
        for player in self._service.list_players():
            print(player)

    def sort(self):
        self._service.sort_players()
