import sys

cookbook = {'Sandwich':
            {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
             'meal': 'lunch',
             'prep_time': 10},
            'Cake':
            {'ingredients': ['flour', 'sugar', 'eggs'],
             'meal': 'dessert',
             'prep_time': 60},
            'Salad':
            {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
             'meal': 'lunch',
             'prep_time': 15}}

def print_recipes_names(cookbook):
    for recipe in cookbook:
        print(f'{recipe}')
    print()

def print_recipe_detail(name):
    if name not in cookbook:
        print(f'"{name}" not found in cookbook\n')
        return None
    print(f'Recipe for {name}:')
    print(f'   Ingredients list: {", ".join(cookbook[name]["ingredients"])}\n'
          f'   To be eaten for {cookbook[name]["meal"]}\n'
          f'   Takes {cookbook[name]["prep_time"]} min of cooking\n')

def delete_receipe(name):
    if name not in cookbook:
        print(f'"{name}" not found in the cookbook\n')
        return None
    del cookbook[name]
    print(f'"{name}" had been deleted from the cookbook\n')

def add_recipe():
    recipe = input('Enter a name:\n')
    print('Enter ingredients:')
    ingredients_list = []
    while True:
        ingredients = sys.stdin.readline()
        if (ingredients == '\n'):
            break
        ingredients_list.append(ingredients[:-1])
    meal = input('Enter a meal type:\n')
    ok = False
    while not ok:
        prep_time = input('Enter a peparation time:\n')
        try:
            prep_time = int(prep_time)
            ok = True
        except ValueError as err:
            print(f'ValueError: {err}')
    cookbook[recipe] = {'ingredients': ingredients_list,
                   'meal': meal,
                   'prep_time': prep_time}

def opt0():
    pass

def opt1():
    add_recipe()

def opt2():
    name = input('Please enter a recipe to delete:\n')
    print()
    delete_receipe(name)

def opt3():
    name = input('Please enter a recipe name to get its details:\n')
    print()
    print_recipe_detail(name)

def opt4():
    print_recipes_names(cookbook)

def opt5():
    print('Cookbook closed. Goodbye !')
    return 1

def print_options():
    print("List of available option:\n"
          "   1: Add a recipe\n"
          "   2: Delete a recipe\n"
          "   3: Print a recipe\n"
          "   4: Print the cookbook\n"
          "   5: Quit\n")

print("Welcome to the Python Cookbook !")
print_options()

cb = [opt0, opt1, opt2, opt3, opt4, opt5]
run = True
while run:
    ok = False
    while not ok:
        option = input("please select an option:\n")
        print()
        try:
            option = int(option)
            if option < 6 and option > 0:
                ok = True
            else:
                print('Sorry, this option doesn\'t exist.')
                print_options()
        except ValueError:
            print('Sorry, this option doesn\'t exist.')
            print_options()
    ret = cb[option]()
    if ret == 1:
        run = False
