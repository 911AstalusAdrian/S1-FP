from lecture.examples.ex17_happyBakery.domain.entitywithid import EntityWithId
from lecture.examples.ex17_happyBakery.domain.recipe import Recipe


class Product(EntityWithId):
    """
    Represents a Bakery Product
    """

    def __init__(self, id_, name, price, recipe):
        super().__init__(id_)
        self._name = name
        self._recipe = recipe
        self.price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Product price <= 0!")
        self._price = value

    @property
    def recipe(self):
        return self._recipe


class ProductValidator:
    @staticmethod
    def validate(product):
        # TODO Implement
        pass
