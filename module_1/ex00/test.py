import time
from book import Book
from recipe import Recipe

x = Book("Incredible Cookbook")

print(f"Cookbook '{x.name}' had just been created at {x.creation_date}\n")

salad = Recipe("salad", 2, 10, ["carrot", "lettuce", "vinegar"], "starter")
pizza = Recipe("pizza", 2, 20, ["tomato", "ham", "mozzarella"], "lunch", "mamamia")
pasta = Recipe("pastas", 2, 15, ["tomato", "beef", "parmigiano"], "lunch", "mamaaa")
cake = Recipe("cake", 3, 30, ["flour", "sugar", "butter", "milk"], "dessert")

x.get_recipe_by_name("bla")

x.add_recipe(salad)

x.get_recipe_by_name("salad")

print(f" - lunch types: {', '.join(x.get_recipes_by_types('lunch'))}")
print(f" - bla types: {x.get_recipes_by_types('bla')}")

time.sleep(0.5)

x.add_recipe(pizza)
x.add_recipe(cake)
x.add_recipe(pasta)

print(f" - starter types: {', '.join(x.get_recipes_by_types('starter'))}")
print(f" - lunch types: {', '.join(x.get_recipes_by_types('lunch'))}")
print(f" - dessert types: {', '.join(x.get_recipes_by_types('dessert'))}")

x.get_recipe_by_name("cake")

la_pizza_de_la_mamaaa = x.get_recipe_by_name("pizza")
print(str(la_pizza_de_la_mamaaa))

print(f"\nCookbook '{x.name}' last update is at {x.last_update}\n")

hey = "coucou"
x.add_recipe(hey)

bad_recipe = Recipe("bad", 2, "h", ["kiwi", "ham", "gravels"], "starter")

print("this shouldn't be printed")
