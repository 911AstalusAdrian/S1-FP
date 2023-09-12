class Cell:
    def __init__(self, value=0):
        # Set the value of the cell; a value of 0 signifies that the cell is in its default state (i.e. empty,
        # not claimed by any player)
        self._value = value

    def is_empty(self):
        """ Check if the cell is empty """
        return self._value == 0

    def is_filled(self):
        """ Check if the cell is filled """
        return not self.is_empty()

    def free_cell(self):
        """ Frees a cell, sets it to its default state """
        self._value = 0

    @property
    def value(self):
        """ Value getter """
        return self._value

    @value.setter
    def value(self, value):
        """ Value setter """
        self._value = value

    def __eq__(self, other):
        """ Overloaded equality method """
        return self._value == other.value
