import unittest

from lecture.examples.ex17_happyBakery.domain.ingredient import Ingredient
from lecture.examples.ex17_happyBakery.domain.product import Product
from lecture.examples.ex17_happyBakery.domain.recipe import Recipe


class IngredientTest(unittest.TestCase):
    def test_ingredient(self):
        ingr = Ingredient(1, "Wheat Flour 000", 5.50)
        self.assertEqual(ingr.id, 1)
        self.assertEqual(ingr.name, "Wheat Flour 000")
        self.assertEqual(ingr.price, 5.50)


class ProductTest(unittest.TestCase):
    def test_product(self):
        p = Product(1, "Super Cake", 15.50, Recipe(100))
        self.assertEqual(p.id, 1)
        self.assertEqual(p.name, "Super Cake")
        self.assertEqual(p.price, 15.50)


class TestIngredient(unittest.TestCase):
    def test_ingredient(self):
        ingr = Ingredient(100, 'Vanilla', 100)
        self.assertEqual(ingr.id, 100)
        self.assertEqual(ingr.name, 'Vanilla')
        self.assertEqual(ingr.price, 100)

    def test_ingr2(self):
        self.assertTrue('nope')