import json
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

ingredients = ["Courgette", "Flour", "Pita", "Lentils", "Yogurt", "Cucumber", "Garlic", "Lemon", "Onion", "Tomato Sauce", "Rice", "Mustard", "Pasta", "Tomato Puree", "Parsley", "Oregano", "Octopus (Canned)", "Spaghetti", "Potatoes", "Chicken", "Beef", "Mince"]
meat = ["Chicken", "Beef", "Mince"]
# recipes=json.load(open("recipes.json"))

class RecipeBook():
    def __init__(self):
        try:
            with open("recipes.json") as f:
                self.recipes = json.load(f)
        except:
            self.recipes = []

    def save(self):
        with open("recipes.json", "w") as f:
            json.dump(self.recipes, f, indent=2)

    def add_recipe(self):
        title = input("Enter recipe title: ").capitalize()
        completer = WordCompleter(ingredients, ignore_case=True)
        ing = list(prompt("Ingredients (comma-separated): ", completer=completer).split(","))

        ing = [i.strip().capitalize() for i in ing]
        print(ing)
        
        for i in ing:
            if i not in ingredients:
                ingredients.append(i)
        notes=input("Add instructions for the recipe or anything else of note:\n").capitalize()

        recipe = {
            "title": title,
            "ingredients": ing,
            "has_meat": any(i in meat for i in ing),
            "notes": notes
        }

        self.recipes.append(recipe)
        self.save_recipes()

    def remove_recipe(self):
        if not self.recipes:
            print("No recipes to remove.")
            return

        for i, r in enumerate(self.recipes, 1):
            print(f"{i}. {r['title']}")

        try:
            idx = int(input("> ")) - 1
            removed = self.recipes.pop(idx)
            print(f"Removed {removed['title']}")
            self.save()
        except:
            print("Invalid selection.")

    def show_all(self):
        print("\nAll Recipes\n-----------")
        for r in self.recipes:
            print(f"\n{r["title"]}")
            for ing in r["ingredients"]:
                print(f"- {ing}")
            print(r["notes"])

    def show_meatless(self):
        print("\nMeatless Recipes\n----------------")
        for r in self.recipes:
            if not r["has_meat"]:
                print(f"\n{r["title"]}")
                for ing in r["ingredients"]:
                    print(f"- {ing}")
                    
    def add_ingredient(self, ingredient :str):
        ingredients.append(ingredient.capitalize())
    
    def remove_ingredient(self, ingredient):
        if ingredient in ingredients:
            ingredients.remove(ingredient)

    def search(self):
        opt = ["By Ingredient", "By Title"]
        choice = self.show_options(opt, "Search mode:")

        if choice == 0:
            completer = WordCompleter(ingredients, ignore_case=True)
            query = prompt("Ingredient: ", completer=completer).lower()
            results = [r for r in self.recipes if query in [i.lower() for i in r["ingredients"]]]
        else:
            titles = [r["title"] for r in self.recipes]
            completer = WordCompleter(titles, ignore_case=True)
            query = prompt("Title: ", completer=completer).capitalize()
            results = [r for r in self.recipes if r["title"] == query]

        if not results:
            print("No results found.")
            return

        for r in results:
            print(f"\n{r['title']}")
            for ing in r["ingredients"]:
                print(f"- {ing}")

    def show_ingredients(self):
        print("Ingredients:")
        for i in ingredients:
            print(f"- {i}")

    def show_options(self, options, message):
        while True:
            print(f"\n{message}")
            for i, opt in enumerate(options, 1):
                print(f"{i}. {opt}")

            try:
                idx = int(input("> ")) - 1
                if idx not in range(len(options)):
                    print("Invalid option.")
                    continue
                return idx
            except:
                print("Enter a number.")

    def save_recipes(self, filename="recipes.json"):
        with open(filename, "w") as fp:
            json.dump([r for r in self.recipes], fp, indent=2)

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

class MainApp():
    def __init__(self):
        self.rb = RecipeBook()

    def run(self):
        opt1 = ["Show Items", "Search", "Add/Remove Item", "Exit"]

        while True:
            ind1 = self.rb.show_options(opt1, "Pick a mode:")
            op1 = opt1[ind1]

            if op1 == "Show Items":
                opt2 = ["Show All Recipes", "Show Meatless Recipes", "Show Ingredients", "Back"]
                ind2 = self.rb.show_options(opt2, "Show:")
                if ind2 == 0:
                    self.rb.show_all()
                elif ind2 == 1:
                    self.rb.show_meatless()
                elif ind2 == 2:
                    self.rb.show_ingredients()

            elif op1 == "Search":
                self.rb.search()

            elif op1 == "Add/Remove Item":
                opt2=["Add Recipe", "Remove Recipe", "Add Ingredient", "Remove Ingredient"]
                ind2=self.rb.show_options(opt2, "Add/Remove:")
                if ind2==0:
                    self.rb.add_recipe()
                    self.rb.save_recipes()
                elif ind2==1:
                    self.rb.remove_recipe()
                    self.rb.save_recipes()
                elif ind2==2:
                    ing=input("Add new ingredient: ")
                    self.rb.add_ingredient(ing)
                    self.save_ingredients()
                else:
                    choice=self.rb.show_options(ingredients, "Select ingredient to remove: ")
                    self.rb.remove_ingredient(ingredients[choice])
                    self.save_ingredients()

            elif op1 == "Exit":
                break

if __name__ == "__main__":
    app = MainApp()
    app.run()
