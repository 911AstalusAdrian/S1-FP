from lecture.examples.ex17_happyBakery.domain.entitywithid import EntityWithId


class Recipe(EntityWithId):
    def __init__(self, id_, *stock_items):
        super().__init__(id_)
        self._stockList = list(stock_items)

    @property
    def ingredients(self):
        """
        List of stock items for recipe
        @return: Reference to the live list of stock items
        """
        return self._stockList


class RecipeValidator:
    @staticmethod
    def validate(recipe):
        # TODO Implement
        pass
