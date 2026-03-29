from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


meat=["Chicken", "Beef", "Mince"]

# by_ingredient = {
    # "chicken": [recipe1, recipe2]
# }

class Recipe():
    ingredients = []
    
    def __init__(self, title :str, ingredients :list):
        self.title = title.capitalize()
        self.has_meat = False if set(ingredients).intersection(meat)==set() else True 
        self.ingredients = ingredients
 
class RecipeBook():
    # TODO find better structure 
    recipes=[]

    def add_recipe(self, recipe :Recipe):
        self.recipes.append(recipe)

    def show_all(self):
        print("\nAll Recipes\n-----------")
        for recipe in self.recipes:
            print(f"{recipe.title}\n{[ing for ing in recipe.ingredients]}")
    
    def show_meatless(self):
        print("\nMeatless Recipes\n----------------")
        for rr in self.recipes:
            if not rr.has_meat:
                print(f"{rr.title}")
                
class RecApp():
    rb=RecipeBook()

    ingredients = ["Courgette", "Flour", "Pita", "Lentils", "Yogurt", "Cucumber", "Garlic", "Lemon", "Onion", "Tomato Sauce", "Rice", "Mustard", "Pasta", "Tomato Puree", "Parsley", "Oregano", "Octopus (Canned)", "Spaghetti", "Potatoes", "Chicken", "Beef", "Mince"]
    
    def add_ingredient(self, ingredient :str):
        ingredients.append(ingredient.capitalize())
        completer = WordCompleter(ingredients, ignore_case=True)

    def create_recipe():
        title='test title'
        # title=input("Enter recipe title: ")
        completer = WordCompleter(ingredients, ignore_case=True)
        ing = map(str.capitalize, ['tomatoes', 'chicken'])

        # ing =  list(prompt("Ingredients (comma-seperated): ", completer=completer).split(","))

        for ingredient in ing:
            if ingredient not in ingredients:
                ingredients.append(str.capitalize(ingredient))

        rb.add_recipe(Recipe(title, ing))

     
def new_recipe():
    # title=input("Enter recipe title: ")
    rb = RecipeBook()
    # TODO autocomplete from a list of ingredients
    rec1 = Recipe("patates", ["Potatoes", "Flour"])
    rec2 = Recipe("withmeat", ["Chicken", "Flour"])
    rb.add_recipe(rec1)
    rb.add_recipe(rec2)
    title = 'test'
    completer = WordCompleter(ingredients, ignore_case=True)
    # ing =  list(prompt("Ingredients (comma-seperated): ", completer=completer).split(","))
    ing = map(str.capitalize, ['tomatoes', 'chicken'])

    for ingredient in ing:
        if ingredient not in ingredients:
            ingredients.append(str.capitalize(ingredient))

    add_recipe(Recipe(title, ing))

    rb.show_all()

new_recipe()
    # rb = RecipeBook()
    # # TODO autocomplete from a list of ingredients
    # rb.add_recipe_inp()
    # rec1 = Recipe("patates", ["Potatoes", "Flour"])
    # rec2 = Recipe("withmeat", ["Chicken", "Flour"])
    # rb.add_recipe(rec1)
    # rb.add_recipe(rec2)
    # rb.show_all()
    # rb.show_meatless()
