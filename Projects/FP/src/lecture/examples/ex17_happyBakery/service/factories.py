from lecture.examples.ex17_happyBakery.domain.ingredient import Ingredient


class IngredientFactory:
    """
    Create validated instances of Ingredient
    """

    def __init__(self, validator):
        self._validator = validator

    def create_ingredient(self, id_, name, price):
        ingr = Ingredient(id_, name, price)
        self._validator.validate(ingr)
        return ingr


"""
Example of starting up layers with Factory pattern

ingr_repo = Repository()
ingr_valid = IngredientValidator()
ingr_factory = IngredientFactory(ingr_valid)
ingr_service = IngredientService(ingr_repo,ingr_factory)
"""
