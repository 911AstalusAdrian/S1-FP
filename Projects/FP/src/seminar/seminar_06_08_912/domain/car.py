"""
Implement the domain class
"""
from seminar.seminar_06_08_912.domain.exceptions import CarException


class Car:
    def __init__(self, id_, license_plate=0, make='', model='', color=''):
        if not isinstance(license_plate, str):
            raise CarException('Invalid value for license_plate!')
        if not isinstance(make, str):
            raise CarException('Invalid value for make!')
        if not isinstance(model, str):
            raise CarException('Invalid value for model!')
        if not isinstance(color, str):
            raise CarException('Invalid value for color!')

        self._id = id_
        self._license_plate = license_plate
        self._make = make
        self._model = model
        self._color = color

    @property
    def id(self):
        return self._id

    @property
    def license_plate(self):
        return self._license_plate

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def color(self):
        return self._color

    def __str__(self):
        return "Id: " + str(self.id) + ", License: " + self.license_plate + ", Car type: " + self.make + ", " + self.model

    def __repr__(self):
        return str(self)
