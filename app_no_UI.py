import requests

# Define a function to call the Nutrition Analysis API
def get_nutrition_info(meal_description):
    api_url = "https://api.edamam.com/api/nutrition-data"
    app_id = "da01367b"
    app_key = "d98cf84f663b417c99035233ddb64989"
    params = {
        "app_id": app_id,
        "app_key": app_key,
        "ingr": meal_description
    }
    response = requests.get(api_url, params=params)
    return response.json()

# Define a function to call the Recipe Search API
def search_recipes(query):
    api_url = "https://api.edamam.com/search"
    app_id = "817ae6ed"
    app_key = "59acde84feee334c2417c752c925f8ac"
    params = {
        "q": query,
        "app_id": app_id,
        "app_key": app_key,
        "to": 5  # Limit to 5 results
    }
    response = requests.get(api_url, params=params)
    return response.json()

# Define a function to call the Food Database API
def get_food_info(food_name):
    api_url = "https://api.edamam.com/api/food-database/v2/parser"
    app_id = "3c30730a"
    app_key = "33f4b48c3971b6d5091d43227f61b966"
    params = {
        "ingr": food_name,
        "app_id": app_id,
        "app_key": app_key
    }
    response = requests.get(api_url, params=params)
    return response.json()

# Define the input meal description
meal_description = "100 gram chicken breast"

# Get nutritional information from the Nutrition Analysis API
nutrition_info = get_nutrition_info(meal_description)

# Print the nutritional analysis
print("Nutritional Analysis:")
print(f"Calories: {nutrition_info['calories']}")
print(f"Proteins: {nutrition_info['totalNutrients']['PROCNT']['quantity']}g")
print(f"Fats: {nutrition_info['totalNutrients']['FAT']['quantity']}g")
print(f"Carbohydrates: {nutrition_info['totalNutrients']['CHOCDF']['quantity']}g")

# Define the search query for the Recipe Search API
recipe_query = "chicken breast"

# Get recipes from the Recipe Search API
recipes = search_recipes(recipe_query)

# Print the first few recipes
print("\nRecipes:")
for recipe in recipes['hits']:
    print(f"Recipe: {recipe['recipe']['label']}")
    print(f"Source: {recipe['recipe']['source']}")
    print(f"URL: {recipe['recipe']['url']}")
    print()

# Define the food name for the Food Database API
food_name = "chicken breast"

# Get food information from the Food Database API
food_info = get_food_info(food_name)

# Print the food database information
print("Food Database Information:")
for food in food_info['hints']:
    food_item = food['food']
    print(f"Food: {food_item['label']}")
    print(f"Category: {food_item['category']}")
    print(f"Category Label: {food_item['categoryLabel']}")
    print(f"Nutrients: {food_item['nutrients']}")
    print()
