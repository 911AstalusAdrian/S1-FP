from unittest import TestCase

from lecture.examples.ex17_happyBakery.domain.exceptions import BakeryException
from lecture.examples.ex17_happyBakery.domain.entitywithid import EntityWithId


class Ingredient(EntityWithId):
    """
    A bakery ingredient
    """

    def __init__(self, id_, name, price):
        super().__init__(id_)
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    def __str__(self):
        return "Ingredient " + str(self.id) + ", " + str(self.name) + ", price " + str(self.price)


'''
Python - PyUnit, ...
Java - JUnit, ...
.NET - NUnit ??
'''


class IngredientValidator:
    @staticmethod
    def validate(ingredient):
        if len(ingredient.name) < 3:
            raise ValueError("Ingredient name must have at least 3 characters.")
        if ingredient.price < 0:
            raise ValueError("Ingredient price < 0!")
