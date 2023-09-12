class Player:
    def __init__(self, player_id, name, strength):
        self._id = player_id
        self._name = name
        self._strength = strength

    def __str__(self):
        return "ID:" + str(self.id) + " | Name: " + self.name.ljust(8) + " | Strength: " + str(self.strength)

    # we use __gt__ for the comparison of two players' strength
    def __gt__(self, other):
        return self.strength > other.strength

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def strength(self):
        return self._strength
