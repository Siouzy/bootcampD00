
cookbook = {}


def create_recipe(ingredients, meal_type, prep_time):
    recipe = {}
    recipe['ingredients'] = ingredients
    recipe['meal'] = meal_type
    recipe['prep_time'] = prep_time
    return recipe


def add_recipe(name, ingredients, meal_type, prep_time):
    global cookbook
    cookbook[name] = create_recipe(ingredients, meal_type, prep_time)


def list_recipes():
    for key, val in cookbook.items():
        print("- %s is a %s that will take you %d minutes" %
              (key, val['meal'], val['prep_time']))


def delete_recipe(name):
    global cookbook
    try:
        del cookbook[name]
    except KeyError:
        print("Not an existing recipe")


def print_recipe(name):
    global cookbook
    try:
        recipe = cookbook[name]
        print("So you want to cook a %s" % name)
        print("You'll need:")
        for ing in recipe['ingredients']:
            print("- %s" % ing)
        print("It is a kind of %s" % recipe["meal"])
        print("The preparation should take you %d minutes" %
              recipe["prep_time"])
    except KeyError:
        print("I don't know this recipe")


def init_cookbook():
    global cookbook
    cookbook['sandwich'] = create_recipe(
        ["ham", "bread", "cheese", "tomatos"],
        "lunch",
        10
        )

    cookbook['cake'] = create_recipe(
        ["flour", "sugar", "eggs"],
        "dessert",
        60
        )

    cookbook['salad'] = create_recipe(
        ["avocado", "arugula", "tomatoes", "spinach"],
        "lunch",
        15
        )


def print_menu():
    print("Please select an option by " +
          "typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")


def get_recipe_features():
    name = input("What is the name of this new recipe ? ")
    ingredients = input("What are the ingredients? " +
                        "Separated by comas. ").split(',')
    meal_type = input("What kind of meal is that ? ")
    try:
        prep_time = int(input("What is the preparation time? In minutes. "))
        add_recipe(name, ingredients, meal_type, prep_time)
    except ValueError:
        print("Not a valide preparation time. Try again.")
        get_recipe_features()


def get_recipe_to_delete():
    name = input("What recipe do you want to delete ? ")
    delete_recipe(name)


def get_recipe_to_print():
    name = input("What recipe do you want to read ? ")
    print_recipe(name)


switcher = {
    1: get_recipe_features,
    2: get_recipe_to_delete,
    3: get_recipe_to_print,
    4: list_recipes
    }

init_cookbook()
while True:
    print_menu()
    try:
        number = int(input('>> '))
        if number == 5:
            print("Goodbye.")
            break
        elif number > 5 or number < 1:
            print("This option does not exist, " +
                  "please type the corresponding number.")
        else:
            switcher[number]()
    except ValueError:
        print("This option does not exist, " +
              "please type the corresponding number.")
