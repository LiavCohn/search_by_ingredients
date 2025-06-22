import json
import sys
from argparse import ArgumentParser
from typing import List
from time import time
import pandas as pd
import re
from consts import MEASUREMENT_WORDS, STOPWORDS,NON_VEGAN_INGREDIENTS,VEGAN_EXCEPTIONS

try:
    from sklearn.metrics import classification_report
except ImportError:
    # sklearn is optional
    def classification_report(y, y_pred):
        print("sklearn is not installed, skipping classification report")


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

def is_ingredient_keto(ingredient: str) -> bool:
    # TODO: Implement (Copy your solution from `nb/src/diet_classifiers.py`)
    return False


def is_ingredient_vegan(ingredient: str) -> bool:

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


def is_keto(ingredients: List[str]) -> bool:
    return all(map(is_ingredient_keto, ingredients))


def is_vegan(ingredients: List[str]) -> bool:
    return all(map(is_ingredient_vegan, ingredients))
