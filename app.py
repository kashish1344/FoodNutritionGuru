from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Define a function to call the Nutrition Analysis API
def get_nutrition_info(meal_description):
    api_url = "https://api.edamam.com/api/nutrition-data"
    app_id = os.getenv('NUTRITION_APP_ID')
    app_key = os.getenv('NUTRITION_APP_KEY')
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
    app_id = os.getenv('RECIPE_APP_ID')
    app_key = os.getenv('RECIPE_APP_KEY')
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
    app_id = os.getenv('FOOD_APP_ID')
    app_key = os.getenv('FOOD_APP_KEY')
    params = {
        "ingr": food_name,
        "app_id": app_id,
        "app_key": app_key
    }
    response = requests.get(api_url, params=params)
    return response.json()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nutrition', methods=['GET', 'POST'])
def nutrition():
    if request.method == 'POST':
        meal_description = request.form['meal_description']
        nutrition_info = get_nutrition_info(meal_description)
        return render_template('nutrition.html', nutrition_info=nutrition_info)
    return render_template('nutrition.html')

@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    if request.method == 'POST':
        recipe_query = request.form['recipe_query']
        recipes = search_recipes(recipe_query)
        return render_template('recipes.html', recipes=recipes['hits'])
    return render_template('recipes.html')

@app.route('/food', methods=['GET', 'POST'])
def food():
    if request.method == 'POST':
        food_name = request.form['food_name']
        food_info = get_food_info(food_name)
        return render_template('food.html', food_info=food_info['hints'])
    return render_template('food.html')

if __name__ == '__main__':
    app.run(debug=True)
