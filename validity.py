def valid(str):
    valid_publishers = ['All Recipes', 'Back to Her Roots', 'BBC Food', 'BBC Good Food', 'Bon Appetit', 'Bunky Cooks', 'Chow', 'Closet Cooking', 'Cookin Canuck', 'Epicurious', 'Food Republic', 'Framed Cooks', 'Healthy Delicious', 'Jamie Oliver', "Lisa's Kitchen"]
    for i in range(len(valid_publishers)):
        if (str == valid_publishers[i]):
            return True
    return False
