from Player.player import Player
from Repository.players_repository import Repository
from Service.service import Service
from UI.ui import UI

player_repository = Repository()
player_service = Service(player_repository)
ui = UI(player_service)

ui.run()