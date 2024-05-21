# Nutrition and Recipe Finder

This project is a Flask-based web application that provides nutrition analysis, recipe search, and food information using the Edamam API. Users can input meal descriptions to get nutritional information, search for recipes, and find detailed food information.

# Demo Video

https://github.com/kashish1344/FoodNutritionGuru/assets/83247791/eac495d8-aa26-4282-a70e-5d1cf6214bc2

## Features

- **Nutrition Analysis:** Input meal descriptions to get detailed nutritional information.
- **Recipe Search:** Search for recipes based on keywords.
- **Food Database:** Get detailed information about specific foods.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/nutrition-recipe-finder.git
    cd nutrition-recipe-finder
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    - Create a `.env` file in the project directory.
    - Add your Edamam API credentials to the `.env` file:
      ```plaintext
      NUTRITION_APP_ID=your_nutrition_app_id
      NUTRITION_APP_KEY=your_nutrition_app_key
      RECIPE_APP_ID=your_recipe_app_id
      RECIPE_APP_KEY=your_recipe_app_key
      FOOD_APP_ID=your_food_app_id
      FOOD_APP_KEY=your_food_app_key
      ```

## Usage

1. **Run the Flask application:**
    ```bash
    python app.py
    ```

2. **Open your browser and navigate to:**
    ```
    http://127.0.0.1:5000/
    ```

3. **Nutrition Analysis:**
    - Go to the Nutrition Analysis page.
    - Enter a meal description and submit to get the nutritional information.

4. **Recipe Search:**
    - Go to the Recipe Search page.
    - Enter a recipe query and submit to get a list of recipes.

5. **Food Database:**
    - Go to the Food Database page.
    - Enter a food name and submit to get detailed information about the food.

## Code Overview

- **`app.py`:** The main Flask application file that sets up the web server and handles API requests.
- **`templates/`:** Directory containing HTML templates for the web interface.

### Core Functions

- **`get_nutrition_info(meal_description)`:** Calls the Edamam Nutrition Analysis API to get nutritional information.
- **`search_recipes(query)`:** Calls the Edamam Recipe Search API to search for recipes.
- **`get_food_info(food_name)`:** Calls the Edamam Food Database API to get food information.

## Dependencies

- Flask
- requests
- python-dotenv
