import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        if not isinstance(name, str):
            print("name must be a string")
            exit(1)

        self.name = name
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.datetime.now()
        self.recipes_list = {"starter" : [], "lunch" : [], "dessert" : []}

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for key, value in self.recipes_list.items():
            for recipe in value:
                if recipe.name == name:
                    print(str(recipe))
                    return recipe
        print(f"'{name}' not found")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type != "starter" and recipe_type != "lunch"\
                and recipe_type != "dessert":
            print(f"'{recipe_type}' is not a good recipe type")
            return None
        recipe_name_list = []
        for recipe in self.recipes_list[recipe_type]:
            recipe_name_list.append(recipe.name)
        return recipe_name_list

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print("recipe must be a Recipe")
            return None
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.datetime.now()
