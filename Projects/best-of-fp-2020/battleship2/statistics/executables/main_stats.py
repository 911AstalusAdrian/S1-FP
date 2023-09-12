from persistence.rules import Rules
from presentation.gui.gui import GUI

# Works with the board setup/configuration from the 'last_board_config' file

Rules().set_rules(test=True, display_probability=False)

nr_of_reps = 100                # How many games will be played
levels_to_test = [1, 2, 3, 4]   # What levels should be tested (1 - beginner, 2 - easy, 3 - medium, 4 - hard)

for i in range(nr_of_reps):
    print(str(i + 1) + '/' + str(nr_of_reps))
    for level in levels_to_test:
        Rules().set_rules(difficulty=level)
        game_session = GUI()
        game_session.run()
