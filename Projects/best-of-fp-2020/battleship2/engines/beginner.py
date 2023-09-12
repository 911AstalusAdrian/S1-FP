from random import randint, choice

from engines.ai import AI
from errors import ServiceError


class BeginnerAI(AI):
    """
    The entry level AI

    Completely randomised ship placement

    Completely randomised shooting (just picks a not already shot cell and shoots it), no strategy
    """
    def _compute_target_coords(self):
        # The target will be a random cell taken from the available_position set
        coords = choice(tuple(self._available_positions))
        self._available_positions.remove(coords)            # remove the chosen target from the set because is not an available position for shooting anymore

        line = coords[0]
        column = coords[1]

        return line, column
