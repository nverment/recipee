import json
from collections import defaultdict
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

ingredients = ["Courgette", "Flour", "Pita", "Lentils", "Yogurt", "Cucumber", "Garlic", "Lemon", "Onion", "Tomato Sauce", "Rice", "Mustard", "Pasta", "Tomato Puree", "Parsley", "Oregano", "Octopus (Canned)", "Spaghetti", "Potatoes", "Chicken", "Beef", "Mince"]

meat=["Chicken", "Beef", "Mince"]

recipes=json.load(open("recipes.json"))
by_ingredient=json.load(open("by_ingredient.json"))

class Recipe():
    ingredients = []
    notes=""
    
    def __init__(self, title :str, ingredients :list, notes :str):
        self.title = title.capitalize()
        self.has_meat = False if set(ingredients).intersection(meat)==set() else True 
        self.ingredients = [ing.capitalize() for ing in ingredients]
        self.notes = notes

    def to_dict(self):
        return {
            "title": self.title,
            "ingredients": self.ingredients,
            "has_meat": self.has_meat,
            "notes": self.notes
        }
 
class RecipeBook():
    # TODO find better structure 
    # recipes=[]

    def add_recipe(self, recipe=None):
        if recipe==None:
            title=input("Enter recipe title: ")
            completer = WordCompleter(ingredients, ignore_case=True)
            ing = list(prompt("Ingredients (comma-seperated): ", completer=completer).replace(" ", "").split(","))

            for ingredient in ing:
                if not ingredient in ingredients:
                    self.add_ingredient(ingredient)
            notes=input("Add instructions for the recipe or anything else of note:\n").capitalize()
            recipe=Recipe(title, ing, notes).to_dict()
        recipes.append(recipe)

    def show_all(self):
        print("\nAll Recipes\n-----------")
        for recipe in recipes:
            print(f"{recipe["title"]}")
            for ing in recipe["ingredients"]:
                print(f"- {ing}")
            print(f"{recipe["notes"]}\n")
    def show_meatless(self):
        print("\nMeatless Recipes\n----------------")
        for recipe in recipes:
            if not recipe["has_meat"]:
                print(f"{recipe["title"]}")
                for ing in recipe["ingredients"]:
                    print(f"- {ing}")
                print(f"{recipe["notes"]}\n")

    def add_ingredient(self, ingredient :str):
        ingredients.append(ingredient.capitalize())

    def search(self, opt=["ing", "title"]):
        if opt=="ing":
            completer = WordCompleter(ingredients, ignore_case=True)
            query = prompt("Ingredient: ", completer=completer).lower()

            results = [
                r for r in recipes
                if query in [ing.lower() for ing in r["ingredients"]]
            ]
        else:
            completer = WordCompleter([r["title"] for r in recipes], ignore_case=True)
            query = prompt("Title: ", completer=completer).capitalize()

            results = [
                r for r in recipes
                if r["title"] == query
            ]
        if not results:
            print("No results found.")
            return
        for r in results:
            print(f"\n{r['title']}")
            for ing in r["ingredients"]:
                print(f"- {ing}")

    def save_recipes(self, filename="recipes.json"):
        with open(filename, "w") as fp:
            json.dump([r for r in recipes], fp, indent=2)

    def save_ingredients(self, filename="ingredients.json"):
        with open(filename, "w") as fp:
            json.dump(ingredients, fp, indent=2)

    def save_by_ingredient(self, filename="by_ingredient.json"):
        data = {
            k: [r.to_dict() for r in v]
            for k, v in by_ingredient.items()
        }
        with open(filename, "w") as fp:
            json.dump(data, fp, indent=2)
    
    def update_json(self):
        # rebuild index
        global by_ingredient
        by_ingredient = defaultdict(list)

        for recipe in self.recipes:
            for ingredient in recipe.ingredients:
                by_ingredient[ingredient.lower()].append(recipe)

        # save all
        self.save_recipes()
        self.save_ingredients()
        self.save_by_ingredient()

    def remove_recipe(self, title):
        global recipes
        recipes = [r for r in recipes if r["title"] != title.capitalize()]
        print(f"recipes now--------\n{recipes}")

    def remove_ingredient(self, ingredient):
        print(ingredient)
        if ingredient in ingredients:
            ingredients.remove(ingredient)
        print(ingredients)
     
    def show_options(self, options_list :list, message):
        while True:
            print(f"\n{message}")
            for i, opt in enumerate(options_list, 1):
                print(f"{i}. {opt}")

            try:
                index = int(input("\n> ")) - 1
                if index not in range(len(options_list)):
                    print("Invalid option, try again.")
                    continue
            except ValueError:
                print("Please enter a number.")
                continue
            return index
        
    def show_ingredients(self):
        print(f"Ingredients:")
        for ingredient in ingredients:
            print(f"- {ingredient}")
            
class MainApp():
    rb = RecipeBook()
    opt1 = ["Show Items", "Search", "Add/Remove Item", "Exit"]
    while True:
        ind1=rb.show_options(opt1, "Pick a mode:")
        op1 = opt1[ind1]
        if op1=="Show Items":
            opt2=["Show All Recipes", "Show Meatless Recipes", "Show All Ingredients", "Go Back"]
            ind2=rb.show_options(opt2, "Show:")
            if ind2==0:
                rb.show_all()
            elif ind2==1:
                rb.show_meatless()
            elif ind2==2:
                rb.show_ingredients()
            else:
                continue
        elif op1=="Search":
            opt2=["Search by Ingredient", "Search by Title", "Go Back"]
            ind2=rb.show_options(opt2, "Search:")
            if ind2==0:
                rb.search("ing")
            elif ind2==1:
                rb.search("title")
            else:
                continue
        elif op1=="Add/Remove Item":
            opt2=["Add Recipe", "Remove Recipe", "Add Ingredient", "Remove Ingredient", "Go Back"]
            ind2=rb.show_options(opt2, "Add/Remove:")
            if ind2==0:
                rb.add_recipe()
                rb.save_recipes()
            elif ind2==1:
                choice=rb.show_options([r["title"] for r in recipes], "Select recipe to remove:")
                rb.remove_recipe([r["title"] for r in recipes][choice])
                rb.save_recipes()
            elif ind2==2:
                ingr=input("Add ingredient: ")
                rb.add_ingredient(ingr)
                rb.save_ingredients()
            elif ind2==3:
                ingr=rb.show_options(ingredients, "Remove ingredient: ")
                rb.remove_ingredient(ingredients[ingr])
                rb.save_ingredients()
            else:
                continue
        elif op1=="Exit":
            break
        