import json
import sys
from argparse import ArgumentParser
from typing import List
from time import time
import pandas as pd
import re
try:
    from sklearn.metrics import classification_report
except ImportError:
    # sklearn is optional
    def classification_report(y, y_pred):
        print("sklearn is not installed, skipping classification report")

NON_VEGAN_INGREDIENTS = {
    'meat': ['beef', 'pork', 'steak','lamb', 'veal', 'chicken', 'turkey', 'duck', 'goose', 'bacon', 'ham', 'sausage', 'pepperoni', 'salami', 'meat', 'poultry', 'game', 'venison', 'rabbit', 'quail', 'pheasant'],
    'dairy': ['milk', 'cream', 'butter', 'cheese', 'yogurt', 'whey', 'casein', 'lactose', 'dairy', 'ghee', 'curd', 'buttermilk', 'sour cream', 'heavy cream', 'half and half'],
    'eggs': ['egg', 'albumen', 'ovalbumin', 'yolk', 'eggs', 'egg white', 'egg yolk'],
    'fish': ['fish', 'salmon', 'tuna', 'cod', 'shrimp', 'prawn', 'crab', 'lobster', 'shellfish', 'anchovy', 'seafood', 'mussel', 'clam', 'oyster', 'squid', 'octopus', 'eel'],
    'honey': ['honey', 'bee pollen', 'royal jelly', 'beeswax'],
    'gelatin': ['gelatin', 'gelatine', 'collagen'],
    'other': ['lard', 'tallow', 'rennet', 'carmine', 'shellac', 'bone', 'marrow', 'broth', 'stock', 'gravy', 'mayonnaise', 'worcestershire sauce']
}

MEASUREMENT_WORDS = {
    'cup', 'cups', 'tablespoon', 'tablespoons', 'teaspoon', 'teaspoons',
    'tsp', 'tbsp', 'oz', 'ounce', 'ounces', 'pound', 'pounds',
    'extract', 'baking', 'powder', 'package', 'can', 'jar',
    'pint', 'quart', 'ml', 'l', 'gram', 'grams', 'kg'
}
STOPWORDS = {
    'a', 'an', 'of', 'and', 'or', 'with', 'the', 'to', 'in', 'for'
}

#helper function to transform a string representation of a list into an actual list of strings
def fix_ingredient_string(s: str) -> List[str]:
    # ex: "[ '1 cup flour''2 tbsp sugar''3 eggs' ]"
    # to: ["1 cup flour", "2 tbsp sugar", "3 eggs"]

    #insert a comma between every string
    s = re.sub(r"'\s*'", "', '", s)

    # try to parse it to a list
    try:
        import ast
        result = ast.literal_eval(s)
        if isinstance(result, list):
            return [str(item).strip() for item in result]
    except Exception:
        pass

    return [s]

def normalize_ingredient(text: str) -> str:
    text = text.lower()
    #clean the ingredient string
    text = re.sub(r'[^a-z\s]', ' ', text)  # remove punctuation/digits
    words = text.split()
    filtered_words = [
        word for word in words
        if word not in MEASUREMENT_WORDS and word not in STOPWORDS
    ]
    return ' '.join(filtered_words)


def is_ingredient_vegan(ingredient: str) -> bool:
    # vegan ingredients that might be confused with non-vegan ones
    VEGAN_EXCEPTIONS = {
        'peanut butter', 'cocoa butter', 'eggless', 'butternut', 'butter beans',
        'coconut milk', 'almond milk', 'soy milk', 'oat milk', 'rice milk',
        'cashew milk', 'hemp milk', 'flax milk', 'pea milk',
        'vegan butter', 'margarine', 'vegan cheese', 'nutritional yeast',
        'vegan mayonnaise', 'vegan cream', 'vegan yogurt'
    }


    norm_ing = normalize_ingredient(ingredient)
    
    for exception in VEGAN_EXCEPTIONS:
        if exception in norm_ing:
            return True
    
    # Check for non-vegan ingredients using word boundaries
    for category, items in NON_VEGAN_INGREDIENTS.items():
        for item in items:
            # Use word boundaries to avoid partial matches
            if re.search(rf'\b{item}\b', norm_ing):
                return False
            
    return True

def is_ingredient_keto(ingredient: str) -> bool:
    # TODO: Implement
    return False

def is_keto(ingredients: List[str]) -> bool:
    return all(map(is_ingredient_keto, ingredients))

def is_vegan(ingredients: List[str]) -> bool:
    return all(map(is_ingredient_vegan, ingredients))



def main(args):
    ground_truth = pd.read_csv(args.ground_truth, index_col=None)
    try:
        start_time = time()
        ground_truth['ingredients'] = ground_truth['ingredients'].apply(lambda x: fix_ingredient_string(x) if isinstance(x, str) else x)
        ground_truth['keto_pred'] = ground_truth['ingredients'].apply(is_keto)
        ground_truth['vegan_pred'] = ground_truth['ingredients'].apply(
            is_vegan)
        ground_truth.to_csv("recepies.csv")
        end_time = time()
    except Exception as e:
        print(f"Error: {e}")
        return -1

    print("===Keto===")
    print(classification_report(
        ground_truth['keto'], ground_truth['keto_pred']))
    print("===Vegan===")
    print(classification_report(
        ground_truth['vegan'], ground_truth['vegan_pred']))
    print(f"== Time taken: {end_time - start_time} seconds ==")
    return 0


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--ground_truth", type=str,
                        default="/usr/src/data/ground_truth_sample.csv")
    sys.exit(main(parser.parse_args()))
