from random import choice

from persistence.last_board_config import LastBoardConfig
from persistence.rules import Rules
from presentation.gui.gui import GUI

orig_display_probability = Rules().display_probability

Rules().set_rules(test=True, display_probability=False)

setups = {
    1: {
        'destroyer':    {'position': 'g3', 'orientation': 'Horizontal'},
        'submarine':    {'position': 'g8', 'orientation': 'Vertical'},
        'cruiser':      {'position': 'g6', 'orientation': 'Vertical'},
        'battleship':   {'position': 'e5', 'orientation': 'Horizontal'},
        'carrier':      {'position': 'c3', 'orientation': 'Horizontal'}
    },
    2: {
        'destroyer':    {'position': 'a1', 'orientation': 'Vertical'},
        'submarine':    {'position': 'a10', 'orientation': 'Vertical'},
        'cruiser':      {'position': 'j1', 'orientation': 'Horizontal'},
        'battleship':   {'position': 'g10', 'orientation': 'Vertical'},
        'carrier':      {'position': 'd1', 'orientation': 'Vertical'}
    },
    3: {
        'destroyer':    {'position': 'a1', 'orientation': 'Horizontal'},
        'submarine':    {'position': 'g4', 'orientation': 'Vertical'},
        'cruiser':      {'position': 'd7', 'orientation': 'Horizontal'},
        'battleship':   {'position': 'c1', 'orientation': 'Horizontal'},
        'carrier':      {'position': 'f10', 'orientation': 'Vertical'}
    },
    4: {
        'destroyer':    {'position': 'd6', 'orientation': 'Vertical'},
        'submarine':    {'position': 'j3', 'orientation': 'Horizontal'},
        'cruiser':      {'position': 'b6', 'orientation': 'Horizontal'},
        'battleship':   {'position': 'd2', 'orientation': 'Vertical'},
        'carrier':      {'position': 'h5', 'orientation': 'Horizontal'}
    },
    5: {
        'destroyer':    {'position': 'e3', 'orientation': 'Vertical'},
        'submarine':    {'position': 'd6', 'orientation': 'Horizontal'},
        'cruiser':      {'position': 'h1', 'orientation': 'Vertical'},
        'battleship':   {'position': 'h7', 'orientation': 'Horizontal'},
        'carrier':      {'position': 'b2', 'orientation': 'Horizontal'}
    },
    6: {
        'destroyer':    {'position': 'j6', 'orientation': 'Horizontal'},
        'submarine':    {'position': 'b3', 'orientation': 'Horizontal'},
        'cruiser':      {'position': 'e3', 'orientation': 'Vertical'},
        'battleship':   {'position': 'j1', 'orientation': 'Horizontal'},
        'carrier':      {'position': 'e9', 'orientation': 'Vertical'}
    },
    7: {
        'destroyer':    {'position': 'd8', 'orientation': 'Horizontal'},
        'submarine':    {'position': 'h2', 'orientation': 'Vertical'},
        'cruiser':      {'position': 'i8', 'orientation': 'Horizontal'},
        'battleship':   {'position': 'a6', 'orientation': 'Horizontal'},
        'carrier':      {'position': 'b3', 'orientation': 'Vertical'}
    },
    8: {
        'destroyer':    {'position': 'a9', 'orientation': 'Horizontal'},
        'submarine':    {'position': 'b2', 'orientation': 'Vertical'},
        'cruiser':      {'position': 'h10', 'orientation': 'Vertical'},
        'battleship':   {'position': 'h2', 'orientation': 'Horizontal'},
        'carrier':      {'position': 'e4', 'orientation': 'Horizontal'}
    },
    9: {
        'destroyer':    {'position': 'b2', 'orientation': 'Horizontal'},
        'submarine':    {'position': 'e6', 'orientation': 'Horizontal'},
        'cruiser':      {'position': 'e1', 'orientation': 'Vertical'},
        'battleship':   {'position': 'g5', 'orientation': 'Vertical'},
        'carrier':      {'position': 'c6', 'orientation': 'Horizontal'}
    },
    10: {
        'destroyer':    {'position': 'a5', 'orientation': 'Horizontal'},
        'submarine':    {'position': 'b10', 'orientation': 'Vertical'},
        'cruiser':      {'position': 'i7', 'orientation': 'Horizontal'},
        'battleship':   {'position': 'e5', 'orientation': 'Horizontal'},
        'carrier':      {'position': 'c3', 'orientation': 'Vertical'}
    }
}
setups_ind = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]        # Change the possible selection of the setups

nr_setups = 5                                       # The number of different setups that will be chosen
nr_of_reps_per_setup = 200                          # How many games will be played on each setup
levels_to_test = [1, 2, 3, 4]                       # What levels should be tested (1 - beginner, 2 - easy, 3 - medium, 4 - hard)

for i in range(nr_setups):
    setup_ind = choice(setups_ind)
    setups_ind.remove(setup_ind)
    print(f"Setup {i + 1}/{nr_setups} ({setup_ind})")
    setup = setups[setup_ind]

    LastBoardConfig().set_config(setup)

    for rep in range(nr_of_reps_per_setup):
        print(f"{rep + 1}/{nr_of_reps_per_setup}")
        for level in levels_to_test:
            Rules().set_rules(difficulty=level)
            game_session = GUI()
            game_session.run()

Rules().set_rules(display_probability=orig_display_probability)
