from pydoc import stripid
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

ingredients = ["Courgette", "Flour", "Pita", "Lentils", "Yogurt", "Cucumber", "Garlic", "Lemon", "Onion", "Tomato Sauce", "Rice", "Mustard", "Pasta", "Tomato Puree", "Parsley", "Oregano", "Octopus (Canned)", "Spaghetti", "Potatoes"]

# by_ingredient = {
    # "chicken": [recipe1, recipe2]
# }

class Recipe():
    ingredients = []
    
    def __init__(self, title :str, ingredients :list, has_meat :bool):
        self.title = title.capitalize()
        self.has_meat = has_meat
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
            if rr.has_meat==False:
                print(rr.title)
                
    def add_ingredient(self, ingredient :str):
        ingredients.append(ingredient.capitalize())
     
    def add_recipe_inp(self):
        title=input("Enter recipe title: ")
        completer = WordCompleter(ingredients, ignore_case=True)
        ing =  list(map(str.capitalize, map(str.strip, prompt("Ingredients (comma-seperated): ", completer=completer).split(","))))
        ans = [True if input("Does it contain meat? [y/n] ").upper()=="Y" else False]

        for ingredient in ing:
            if ingredient not in ingredients:
                if input(f"{ingredient} not in ingredient list. Add (y/n)? ").capitalize()=="Y":
                    self.add_ingredient(ingredient) 

        rec = Recipe(title, ing, ans)
        self.recipes.append(rec)
        return rec

if __name__ == "__main__":
    rb = RecipeBook()
    # TODO autocomplete from a list of ingredients
    rb.add_recipe_inp()
    rec1 = Recipe("patates", ["Potatoes", "Flour"], False)
    rb.add_recipe(rec1)
    rb.show_all()
    # rb.show_meatless()
    # completer = WordCompleter(ingredients, ignore_case=True)
    # user_input = prompt("Ingredient: ", completer=completer)