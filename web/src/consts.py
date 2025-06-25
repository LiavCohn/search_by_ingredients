NON_VEGAN_INGREDIENTS = {
    'meat': ['beef', 'pork', 'steak','lamb', 'veal', 'chicken', 'turkey', 'duck', 'goose', 'bacon', 'ham', 'sausage', 'pepperoni', 'salami', 'meat', 'poultry', 'game', 'venison', 'rabbit', 'quail', 'pheasant'],
    'dairy': ['milk', 'cream', 'butter', 'cheese', 'yogurt', 'whey', 'casein', 'lactose', 'dairy', 'ghee', 'curd', 'buttermilk', 'sour cream', 'heavy cream', 'half and half'],
    'eggs': ['egg', 'albumen', 'ovalbumin', 'yolk', 'eggs', 'egg white', 'egg yolk'],
    'fish': ['fish', 'salmon', 'tuna', 'cod', 'shrimp', 'prawn', 'crab', 'lobster', 'shellfish', 'anchovy', 'seafood', 'mussel', 'clam', 'oyster', 'squid', 'octopus', 'eel'],
    'honey': ['honey', 'bee pollen', 'royal jelly', 'beeswax'],
    'gelatin': ['gelatin', 'gelatine', 'collagen'],
    'other': ['lard', 'tallow', 'rennet', 'carmine', 'shellac', 'bone', 'marrow', 'broth', 'stock', 'gravy', 'mayonnaise', 'worcestershire sauce']
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

MANUAL_KETO_OVERRIDES = {
    'garbanzo bean':61,
    'salmon': 0.0,
    'chicken': 0.0,
    'pesto': 4.0,
    'avocado': 2.0,
    'bacon': 1.4,
    'mayonnaise': 1.0,
    'almond flour': 10.0,
    'coconut flour': 16.0,
    'zucchini': 2.1,
    'shrimp': 0.0,
    'cod': 0.0,
    'tuna': 0.0,
    'beef': 0.0,
    'pork': 0.0,
    'lamb': 0.0,
    'stevia': 0.0,
    'erythritol': 0.0,
    'water': 0.0,
    'lemon': 3.0,
    'banana': 23.0,
    'lime': 3.0,
}

MEASUREMENT_WORDS = {
    'cup', 'cups', 'tablespoon', 'tablespoons', 'teaspoon', 'teaspoons',
    'tsp', 'tbsp', 'oz', 'ounce', 'ounces', 'pound', 'pounds', 'ml', 'l', 'gram',
    'grams', 'kg', 'pint', 'quart', 'drops', 'pinch', 'dash', 'slice', 'slices',
    'piece', 'pieces', 'clove', 'cloves', 'head', 'heads', 'leaf', 'leaves',
    'sprig', 'sprigs', 'handful', 'bunch', 'block', 'stick', 'strip', 'cube',
    'chunks', 'scoop', 'portion','jar','can','inch','package','hulled','shelled','can','cans'
}
PREPARATION_WORDS = {
    'diced', 'shredded', 'chopped', 'melted', 'grated', 'minced', 'cut',
    'sliced', 'crushed', 'peeled', 'roasted', 'boiled', 'baked', 'steamed',
    'blanched', 'cooked', 'raw', 'fresh', 'frozen', 'dry', 'ground', 'trimmed',
    'washed', 'cleaned', 'soaked', 'marinated', 'seasoned', 'spiced', 'riped',
    'pitted', 'optional','baking','freshly','taste'
}
SIMPLIFY_MAP = {
    'unsalted butter': 'butter',
    'salted butter': 'butter',
    'egg yolk': 'egg',
    'egg white': 'egg',
    'mozzarella': 'mozzarella cheese',
    'parmesan': 'parmesan cheese',
    'ricotta': 'ricotta cheese',
    'heavy whipping cream': 'heavy cream',
    'mayonnaise': 'mayonnaise',
    'cream cheese': 'cream',
    'chicken breast': 'chicken',
    'chicken thighs': 'chicken',
    'salmon fillet': 'salmon',
    'ground beef': 'beef',
    'ground pork': 'pork',
    'ground lamb': 'lamb',
    'shrimp': 'shrimp',
    'cod fillet': 'cod',
    'tuna steak': 'tuna',
    'scallions': 'green onion',
    'splenda calorie sweetener granulated': 'splenda',
    'splenda calorie free sweetener granulated': 'splenda',
    'splenda calorie free sweetener': 'splenda',
    'splenda calorie sweetener': 'splenda',
    'splenda calorie free sweetener': 'splenda',
    'splenda calorie free sweetener': 'splenda',
    'garlic salt':'salt',
    'kosher salt':'salt',
    'brown sugar':'sugar',
    'white sugar':'sugar',
    'confectioners sugar':'sugar',
    'powdered sugar':'sugar',
    'vanilla ice cream':'ice cream',
    'chocolate ice cream':'ice cream',
    'strawberry ice cream':'ice cream',
    'mint ice cream':'ice cream',
    'coffee ice cream':'ice cream',
    'caramel ice cream':'ice cream',
    'cherry ice cream':'ice cream',
}

COMMON_DESCRIPTORS = [
    'cut into chunks', 'cut into pieces', 'minced', 'fresh', 'dried', 'chopped', 'sliced', 'grated', 'shredded','pre-cooked','pre-baked',
    'ground', 'peeled', 'seeded', 'zested', 'juiced', 'thinly', 'cleaned', 'with skin', 'without skin', 'with bone', 'boneless', 'skinless', 'drained', 'rinsed', 'optional', 'to taste', 'needed', 'as needed', 'halved', 'quartered', 'cubed', 'crumbled', 'softened', 'melted', 'beaten', 'large', 'small', 'medium', 'extra-virgin', 'extra virgin', 'unsalted', 'salted', 'whole', 'raw', 'cooked', 'baked', 'roasted', 'steamed', 'boiled', 'blanched', 'frozen', 'warm', 'hot', 'cold', 'room temperature', 'finely', 'coarsely', 'prepared', 'pressed', 'thin', 'thick', 'shelled', 'pitted', 'seedless', 'ripe', 'overripe', 'unripe', 'organic', 'lowfat', 'nonfat', 'full fat', 'reduced fat', 'fat free', 'part skim', 'low moisture', 'moisture', 'plain', 'flavored', 'sweetened', 'unsweetened', 'light', 'dark', 'extra', 'super', 'classic', 'premium', 'original', 'natural', 'artificial', 'imitation', 'pasteurized', 'unpasteurized', 'homemade', 'store bought', 'store-bought', 'brand', 'type', 'variety', 'style', 'grade', 'quality', 'imported', 'domestic', 'local', 'wild', 'farm', 'farm raised', 'wild caught', 'canned', 'bottled', 'jarred', 'packaged', 'boxed', 'bagged', 'bulk', 'loose', 'whole grain', 'refined', 'enriched', 'fortified', 'sprouted', 'ancient grain', 'heirloom', 'baby', 'mini', 'giant', 'jumbo', 'large', 'small', 'medium', 'extra large', 'extra small', 'petite', 'bite size', 'bite-size', 'snack size', 'snack-size', 'family size', 'family-size', 'party size', 'party-size', 'single serve', 'single-serve', 'double', 'triple', 'quadruple', 'half', 'quarter', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'dozen', 'half dozen', 'baker', "baker's", 'bakers', 'packed', 'cored'
]

KETO_AROMATICS = {
    'garlic', 'shallot', 'ginger', 'scallion', 'chive', 'parsley', 'basil', 'oregano', 'thyme', 'rosemary',
    'pepper', 'black pepper', 'onion powder', 'garlic powder', 'dill', 'cilantro', 'sage', 'mint', 'coriander',
    'cumin', 'smoked paprika','paprika', 'nutmeg', 'clove', 'bay leaf', 'red pepper flake', 'cayenne', 'marjoram', 'tarragon',
    'lemon zest','lemon juice','curry powder', 'herbes de provence', 'italian seasoning', 'five spice', 'zaatar', 'sumac',
    'caraway', 'anise', 'star anise', 'savory', 'fenugreek', 'wasabi', 'horseradish', 'mace', 'saffron', 'sesame seed',
    'poppy seed', 'celery seed', 'vanilla extract', 'cinnamon', 'lemongrass', 'galangal', 'ajwain', 'asafoetida',
    'amchur', 'rose water', 'orange blossom water', 'lavender', 'edible flowers', 'spice', 'spices', 'herb', 'herbs',
    'ginger root','lemon peel','green onion','pepper','salt','garlic salt','cayenne pepper'
}