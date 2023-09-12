class Player:
    """
    Player entity
    """
    def __init__(self, player_type, player_id, piece):
        if player_type not in ('h', 'c'):
            raise TypeError("Invalid  player type: " + player_type)
        self._type = player_type  # the player type; 'h' - human or 'c' - computer
        self._id = player_id  # the players id
        self._piece = piece  # the players piece symbol (UI) or piece png file name (GUI)

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, player_type):
        self._type = player_type

    @property
    def id(self):
        return self._id

    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, piece):
        self._piece = piece
