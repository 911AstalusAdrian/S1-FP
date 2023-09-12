from persistence.rules import Rules
from presentation.gui.gui import GUI
from presentation.ui import UI

show_the_strategy_on_hard_difficulty = True
Rules().set_rules(test=False, display_probability=show_the_strategy_on_hard_difficulty)

game_session = GUI()
game_session.run()

