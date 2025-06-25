# ==========================================================
# Author: Liav Cohn
# This code is provided for evaluation purposes only.
# ==========================================================

from typing import List
import re
from helpers import is_ingredient_keto as is_ingredient_keto_helper,normalize_ingredient_vegan
from consts import NON_VEGAN_INGREDIENTS,VEGAN_EXCEPTIONS

try:
    from sklearn.metrics import classification_report
except ImportError:
    # sklearn is optional
    def classification_report(y, y_pred):
        print("sklearn is not installed, skipping classification report")





def is_ingredient_keto(ingredient: str) -> bool:
    return is_ingredient_keto_helper(ingredient)


def is_ingredient_vegan(ingredient: str) -> bool:

    norm_ing = normalize_ingredient_vegan(ingredient)
    
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


def is_keto(ingredients: List[str]) -> bool:
    return all(map(is_ingredient_keto, ingredients))


def is_vegan(ingredients: List[str]) -> bool:
    return all(map(is_ingredient_vegan, ingredients))
