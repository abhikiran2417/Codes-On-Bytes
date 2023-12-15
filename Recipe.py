import requests

def get_recipes(api_id, api_key, ingredients):
    base_url = 'https://www.edamam.com/results/recipes'
    params = {
        'q': '',
        'app_id': api_id,
        'app_key': api_key,
        'ingr': ingredients,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get('hits', [])
    else:
        print(f"Error: {response.status_code}")
        return []

def display_recipes(recipes):
    if not recipes:
        print("No recipes found.")
        return

    for index, hit in enumerate(recipes, 1):
        recipe = hit['recipe']
        print(f"\n{index}. {recipe['label']}")
        print(f"   {recipe['url']}")

def main():
    print("Welcome to the Recipe Search App!")
    api_id = 'd4b94734'
    api_key = '9d1719c567ce0ddca653cbee11a57be3'
    ingredients = input("Enter the ingredients you have (comma-separated): ").strip()

    recipes = get_recipes(api_id, api_key, ingredients)

    print("\nSearch Results:")
    display_recipes(recipes)

if __name__ == "__main__":
    main()
