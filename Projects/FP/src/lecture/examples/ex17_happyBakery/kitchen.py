from lecture.examples.ex17_happyBakery.domain.ingredient import Ingredient, IngredientValidator
from lecture.examples.ex17_happyBakery.domain.product import Product
from lecture.examples.ex17_happyBakery.domain.recipe import Recipe
from lecture.examples.ex17_happyBakery.domain.stock import Stock
from lecture.examples.ex17_happyBakery.repository.repository import Repository
from lecture.examples.ex17_happyBakery.repository.textrepository import IngredientTextFileRepository
from lecture.examples.ex17_happyBakery.service.factories import IngredientFactory

import pickle


def create_ingredient_repo():
    repo = IngredientTextFileRepository()
    repo.store(Ingredient(100, "Bread Flour (White, 550)", 1))
    repo.store(Ingredient(101, "Yeast (dry)", 15))
    repo.store(Ingredient(102, "Sugar (white)", 24))
    repo.store(Ingredient(103, "Salt (regular)", 30))
    repo.store(Ingredient(104, "Oil (canola)", 55))
    repo.store(Ingredient(105, "Butter", 60))
    repo.store(Ingredient(106, "Egg (chicken)", 8))
    repo.store(Ingredient(107, "Cake flour", 2))
    repo.store(Ingredient(108, "Baking powder", 12))
    repo.store(Ingredient(109, "Vanilla (extract)", 80))
    return repo


'''
This is my super duper text file:

100;Bread Flour (White, 550);1
101;Yeast (dry);15
'''

# repo = create_ingredient_repo()
# print(len(repo))
# print(repo[104])

'''
1. Write to/read from a text file
2. Write to/read from a binary file
'''

# repo = Repository()
repo = IngredientTextFileRepository("ingr.txt")
print(len(repo))
# print(repo[104])


def write_text_file(repo):
    # C:\FP\bakery\blabla
    # ../.../ingredients.txt
    f = open('ingredients.txt', 'wt')
    for id_ in range(100, 110):
        ingr = repo[id_]
        line = str(ingr.id) + ';' + ingr.name + ';' + str(ingr.price)
        f.write(line)
        f.write('\n')
    f.close()


def read_text_file():
    f = open('ingredients.txt', 'rt')  # read text
    lines = f.readlines()
    f.close()

    factory = IngredientFactory(IngredientValidator())
    repo = Repository()

    for line in lines:
        line = line.split(';')
        repo.store(factory.create_ingredient(int(line[0]), line[1], int(line[2])))
    return repo


def write_bin_file(repo):
    f = open('ingredients.bin', 'wb')  # read text
    pickle.dump(repo, f)
    f.close()


def read_bin_file():
    f = open('ingredients.bin', 'rb')  # read text
    repo = pickle.load(f)
    f.close()
    return repo


# repo = read_text_file()
# write_bin_file(repo)
# repo = read_bin_file()
# print(len(repo))
# print(repo[104])


# write_text_file(repo)
# repo = read_text_file()


def create_bread_recipe(ingredients_repo):
    """
    1 package (1/4 ounce) active dry yeast
    2-1/4 cups warm water (110° to 115°)
    3 tablespoons sugar plus 1/2 teaspoon sugar
    1 tablespoon salt
    2 tablespoons canola oil
    6-1/4 to 6-3/4 cups bread flour
    source: https://www.tasteofhome.com/recipes/basic-homemade-bread/
    """
    recipe = Recipe(500)
    recipe.ingredients.append(Stock(ingredients_repo[101], 20))
    recipe.ingredients.append(Stock(ingredients_repo[102], 30))
    recipe.ingredients.append(Stock(ingredients_repo[103], 5))
    recipe.ingredients.append(Stock(ingredients_repo[104], 10))
    recipe.ingredients.append(Stock(ingredients_repo[100], 1000))
    return recipe


def create_cake_recipe(ingredients_repo):
    """
    175g (6oz) margarine or softened butter
    175g (6oz) caster sugar
    3 large eggs
    175g (6oz) self-raising flour, sifted
    1tsp baking powder
    1tsp vanilla extract
    pinch of salt
    source: https://www.houseandgarden.co.uk/recipe/simple-vanilla-cake-recipe
    """
    recipe = Recipe(501)
    recipe.ingredients.append(Stock(ingredients_repo[105], 175))
    recipe.ingredients.append(Stock(ingredients_repo[102], 175))
    recipe.ingredients.append(Stock(ingredients_repo[106], 3))
    recipe.ingredients.append(Stock(ingredients_repo[107], 175))
    recipe.ingredients.append(Stock(ingredients_repo[108], 5))
    recipe.ingredients.append(Stock(ingredients_repo[109], 5))
    recipe.ingredients.append(Stock(ingredients_repo[103], 2))
    return recipe


def create_product_repo():
    product_repo = Repository()
    ingredients_repo = create_ingredient_repo()
    product_repo.store(Product(200, "Homemade bread", 120, create_bread_recipe(ingredients_repo)))
    product_repo.store(Product(201, "Vanilla cake", 340, create_cake_recipe(ingredients_repo)))
    return product_repo


'''
Lecture 8 TODOs 
'''
