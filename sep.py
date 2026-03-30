import json
from collections import defaultdict
from pprint import pprint
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

ingredients = ["Courgette", "Flour", "Pita", "Lentils", "Yogurt", "Cucumber", "Garlic", "Lemon", "Onion", "Tomato Sauce", "Rice", "Mustard", "Pasta", "Tomato Puree", "Parsley", "Oregano", "Octopus (Canned)", "Spaghetti", "Potatoes", "Chicken", "Beef", "Mince"]

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

    def to_dict(self):
        return {
            "title": self.title,
            "ingredients": self.ingredients,
            "has_meat": self.has_meat
        }
 
class RecipeBook():
    # TODO find better structure 
    recipes=[]

    def add_recipe(self, recipe=None):
        if recipe==None:
            title=input("Enter recipe title: ")
            completer = WordCompleter(ingredients, ignore_case=True)
            ing =  list(prompt("Ingredients (comma-seperated): ", completer=completer).split(","))

            for ingredient in ing:
                if ingredient not in ingredients:
                    add_ingredient(str.capitalize(ingredient))
            recipe=Recipe(title, ing)
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
                
    def add_ingredient(self, ingredient :str):
        ingredients.append(ingredient.capitalize())

    def search_by_ingredient(ingredient :str):
        if not ingredient in by_ingredient:
            print("not found")
        res = by_ingredient[ingredient.lower()]
        for r in res:
            print(f"- {res.title}\n{[ing for ing in res.ingredients]}")


     
rb = RecipeBook()
rec1 = Recipe("patates", ["Potatoes", "Flour"])
rec2 = Recipe("withmeat", ["Chicken", "Flour"])
rb.add_recipe(rec1)
rb.add_recipe(rec2)
rb.show_all()

by_ingredient = defaultdict(list) 

for recipe in rb.recipes:
    for ingredient in recipe.ingredients:
        by_ingredient[ingredient.lower()].append(recipe)

with open('by_ingredient.json', "w") as fp:
    json.dump(by_ingredient, fp)
