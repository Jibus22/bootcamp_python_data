import copy

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, recipe_type, description = ''):
        if not isinstance(name, str):
            print("name must be a string")
            exit(1)
        if not isinstance(recipe_type, str):
            print("recipe_type must be a string")
            exit(1)
        if not isinstance(description, str):
            print("description must be a string")
            exit(1)
        if not isinstance(cooking_lvl, int):
            print("cooking_lvl must be an int")
            exit(1)
        if not isinstance(cooking_time, int):
            print("cooking_time must be an int")
            exit(1)
        if not isinstance(ingredients, list):
            print("ingredients must be a list")
            exit(1)
        for elem in ingredients:
            if not isinstance(elem, str):
                print("ingredients elements must be string")
                exit(1)

        if (cooking_lvl < 1 and cooking_lvl > 5):
            print("cooking lvl must be 1 <= x <= 5")
            exit(1)
        if (cooking_time < 0):
            print("cooking_time must be positive")
            exit(1)
        if (recipe_type != "starter" and recipe_type != "lunch"\
                and recipe_type != "dessert"):
            print("recipe_type must either be 'starter', 'lunch' or 'dessert'")
            exit(1)

        self.name = name
        self.recipe_type = recipe_type
        self.description = description
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = copy.deepcopy(ingredients)

    def __str__(self):
        return (f"{self.name} recipe: {self.description}\n"
                f"   Ingredients: {', '.join(self.ingredients)}\n"
                f"   Cook {self.cooking_time} minutes. "
                f"   Difficulty: {self.cooking_lvl}\n"
                f"   Meal to eat for {self.recipe_type}")
