from datetime import datetime

def get_day_info():
    dt = datetime.now()
    dnum = dt.weekday()
    day = dt.strftime('%A').lower()
    return dnum, day

dnum, day = get_day_info()

food_types = ["legumes", "chicken", "ladero", "ground meat", "carbs", "seafood", "red meat"]
food_type = food_types[dnum]

legumes = {
    "beans and taters": {"black beans", "potatoes", "tomato sauce", "tomato paste", "harissa", "onion"}
}

chicken = {
    "mushrooms and rice": {"mushrooms", "tomato paste", "tomato sauce", "harissa", "rice", "chicken cube"},
    "kati pou tha ftiaksei h anthi": {"anthi"}
}

ladero = {
    "patates giaxni": {"potatoes", "tomato sauce"}
}

ground_meat = {
    "chili": {"ground meat", "tomato paste", "tomato sauce", "harissa", "onions", "carrots", "potatoes"},
    "soy mince pasta": {"pasta", "soy ground meat", "tomato paste", "tomato sauce", "harissa", "onions", "cheese"},
    "mince pasta": {"pasta", "ground meat", "tomato paste", "tomato sauce", "harissa", "onions", "cheese"}
}

carbs = {
    "potato salad": {"potatoes", "mustard", "mayonaisse", "lemon", "vinegar", "yoghurt", "cucumber", "onion"},
    "potato balls": {"potatoes", "flour", "eggs"},
    "gnocchi": {"gnocchi", "heavy cream", "cheese", "mushrooms"},
    "onion pasta": {"pasta", "onions", "tomato paste", "paprika", "heavy cream"}
}

seafood = {
    "shrimp pasta" : {"shrimp", "pasta", "milk", "lemon", "garlic", "flour"},
    "shrimp fried rice": {"rice", "egg", "shrimp", "soy sauce", "onions"}
}

red_meat = {}

all_recipes = [legumes, chicken, ladero, ground_meat, carbs, seafood, red_meat]

def todays_recipes():
    return all_recipes[dnum]

def find_by_ingredient(avail_ingredients, trec):
    possible_recipes = []
    for recipe, ingredients in trec.items():
        if avail_ingredients.issubset(ingredients):
            possible_recipes.append(recipe)
    
    if possible_recipes:
        print("you can cook:", ", ".join(possible_recipes))
    else:
        print("no recipes found :(\n")
    print("\n")
    # display_recipes(possible_recipes)
    return possible_recipes    

def display_recipes(trec):
    print(f"displaying all recipes for {day}, category {food_type}:")
    for recipe in trec.keys():
        print(f"- {recipe}")
    
    display_mode = input("\ndisplay ingredients for all recipes? (y/n)\n").strip().lower()
    if display_mode == "y":
        for recipe, ingredients in trec.items():
            print(f"\n{recipe}:\ningredients:")
            for ingredient in ingredients:
                print(f"- {ingredient}")

def main():
    while True:
        print(f"today it is:\t{day}\nfood type:\t{food_type}")
        trec = todays_recipes()
        user_input = input("\nselect cooker mode: \n- [0]\tdisplay all recipes from this category\n- [1]\tsearch for recipe by ingredients\n- [exit] quit program\n").strip().lower()
        
        if user_input == "exit":
            print("goodbye!")
            break
        
        if user_input == "0":
            display_recipes(trec)
        elif user_input == "1":
            avail_ingredients = set(input("enter ingredients you have in the fridge: ").lower().split(", "))
            rec = find_by_ingredient(avail_ingredients, trec)
            display_recipes(rec)
        else:
            print("invalid input - please select 0, 1, or type 'exit' to quit.")

if __name__ == "__main__":
    main()
