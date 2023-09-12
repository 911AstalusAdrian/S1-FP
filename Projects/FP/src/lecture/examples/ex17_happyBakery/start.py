"""
The Happy Bakery is a family-run business that produces and sells bakery and confectionary products.
The bakery turns ingredients into delicious products using defined recipes.
They need you, yes you! to help them manage their daily workflow.
What does this entail?
    a. Manage available ingredients, recipes and products that the bakery knows to make
    b. Record a production run. This transforms existing ingredients into product, according to the recipe
    c. Keep the stock for each ingredient and product
    e. Show used ingredients, sorted in descending order of amount used.

How do I analyze a problem statement? (problem -> working program)

1. What is the problem domain?
   What are the problem entities?
       Ingredient
       Recipe
       Product
       Stock (Ingredient or Product | quantity - int for simplicity)

    How are the entities related?
        Recipe -> Stock (one or several - represents what you need to bake the cake)
        Product <-> Recipe (one to one)

    How much of each Ingredient / Product do we have?
        - use a list / dictionary

    How does our layered architecture application look like?

    UI -> Functions / Service / Controller -> Repository
                                              (? database)

2. What do I start with (according to simple feature-driven development)
    - Start with 1 entity and 1 functionality
    - Make 1 thing work well
    - Fix all coding errors ASAP!!


    Lecture 6 - Manage stock

    Lecture 8 - Service & other shiny new things
        1. Repository - at least 2 valid options
            a. Create a Repo class for each entity (IngredientRepo, Product Repo etc.)
                + treat special cases (e.g. product does something ingredient does not)
                - several Repo classes (more code to write, test, debug)

            b. Create a single, generic Repository class
                How do we use this?
                    ingredient_repo = Repo()
                    product_repo = Repo()
                + just one class to write, test, debug
                - restrict to the common implementation of entities

                Let's set the constraint the each entity has a unique id (uses the id property)

            c. A generic Repository class + inheritance to handle specifics (c = a + b)
                - you have to know how to use inheritance
"""
