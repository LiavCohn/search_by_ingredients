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

# vegan ingredients that might be confused with non-vegan ones
VEGAN_EXCEPTIONS = {
        'peanut butter', 'cocoa butter', 'eggless', 'butternut', 'butter beans',
        'coconut milk', 'almond milk', 'soy milk', 'oat milk', 'rice milk',
        'cashew milk', 'hemp milk', 'flax milk', 'pea milk',
        'vegan butter', 'margarine', 'vegan cheese', 'nutritional yeast',
        'vegan mayonnaise', 'vegan cream', 'vegan yogurt'
    }