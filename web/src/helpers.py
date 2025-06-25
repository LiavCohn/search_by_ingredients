from functools import lru_cache
import re
import pandas as pd
import numpy as np
from rapidfuzz import process, fuzz
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from consts import KETO_AROMATICS, MEASUREMENT_WORDS,PREPARATION_WORDS,SIMPLIFY_MAP,COMMON_DESCRIPTORS,MANUAL_KETO_OVERRIDES


lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_df() -> None:
    global df_lookup
    global df
    df = pd.read_csv("web/carbs.csv")
   
    df = df.dropna(subset=["carbohydrate_g", "description"])
    df = df[df["carbohydrate_g"].apply(lambda x: isinstance(x, (int, float, np.integer, np.floating)) or str(x).replace('.', '', 1).isdigit())]
    df["carbohydrate_g"] = df["carbohydrate_g"].astype(float)

    df['normalized_description'] = df['description'].apply(normalize_ingredient_keto)
    df_lookup = dict(zip(df['normalized_description'], df['carbohydrate_g']))


def normalize_ingredient_vegan(text: str) -> str:
    text = text.lower()
    #clean the ingredient string
    text = re.sub(r'[^a-z\s]', ' ', text)  # remove punctuation/digits
    words = text.split()
    filtered_words = [
        word for word in words
        if word not in MEASUREMENT_WORDS and word not in stop_words
    ]
    return ' '.join(filtered_words)


def normalize_ingredient_keto(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    words = word_tokenize(text)
    filtered = [lemmatizer.lemmatize(w) for w in words if w not in stop_words and w not in MEASUREMENT_WORDS and w not in PREPARATION_WORDS]
    norm = ' '.join(filtered)
    for k, v in SIMPLIFY_MAP.items():
        if k in norm:
            norm = v
    for desc in COMMON_DESCRIPTORS:
        norm = norm.replace(desc, '').strip()
    if not norm or norm in {"", "and", "or", "with", "the"}:
        return text
    return norm


@lru_cache(maxsize=1024)
def get_carbs_for_ingredient_cached(norm_ing, orig_ing):
    # Manual override
    if norm_ing in MANUAL_KETO_OVERRIDES:
        return MANUAL_KETO_OVERRIDES[norm_ing]
    # Fast dict lookup
    if norm_ing in df_lookup:
        return df_lookup[norm_ing]
    # Substring/whole-word match in USDA
    for k in df_lookup:
        if norm_ing in k or k in norm_ing:
            return df_lookup[k]
    # Fuzzy match as last resort
    match, score, _ = process.extractOne(norm_ing, list(df_lookup.keys()), scorer=fuzz.token_set_ratio)
    if score >= 80:
        return df_lookup[match]
    return None

def get_carbs_for_ingredient(ingredient):
    norm_ing = normalize_ingredient_keto(ingredient)
    carbs = get_carbs_for_ingredient_cached(norm_ing, ingredient)
    if carbs is not None:
        return carbs
    return 0.0

def is_ingredient_keto(ingredient, carb_limit=10):
    norm = normalize_ingredient_keto(ingredient)
    if norm in KETO_AROMATICS:
        return True
    carbs = get_carbs_for_ingredient(ingredient)
    if carbs is None:
        return True
    if carbs > carb_limit:
        return False
    return True