from random import choice

from engines.ai import AI
from engines.easy import EasyAI


class MediumAI(EasyAI):
    """
    Medium level AI

    Randomised ship placement

    Randomised shooting + hunting when hitting a ship:

    Strategy:
        Identical to the EasyAI but the number of possible random shots is reduced to half
        (since the smallest ship has length 2, there is enough to shoot only the even (or only the even) position
        to guarantee that all the ships are hit at least once)
    """

    def _compute_available_positions(self):
        # The initially available positions are only the even position
        # Creating a chessboard-like pattern for the available positions

        av_pos = set()
        for i in range(self._edge_length):
            if i % 2 == 0:
                for j in range(1, self._edge_length, 2):
                    av_pos.add((i + 1, j + 1))
            else:
                for j in range(0, self._edge_length, 2):
                    av_pos.add((i + 1, j + 1))

        return av_pos
