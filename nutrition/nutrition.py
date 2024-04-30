# https://cs50.harvard.edu/python/2022/psets/2/nutrition/

def food():
    rawfruit = input("Item: ").lower().title()
    caloriesoutput = checkfood(rawfruit)
    if caloriesoutput = caloriesoutput.isdigit():
        print("Calories:", caloriesoutput)





def checkfood(rf):
    fruits = {"Apple": 130, "Avocado": 50, "Banana": 110, "Cantaloupe": 50,
              "Grapefruit": 60, "Grapes": 90, "Honeydrew Melon": 50, "Kiwifruit": 90,
              "Lemon": 15, "Lime": 20, "Nectarine": 60, "Orange": 80, "Peach": 60, "Pear": 100,
              "Pineapple": 50, "Plums": 70, "Strawberries": 50, "Sweet Cherries": 100,
              "Tangerine": 50, "Watermelon": 80}
    if rf in fruits:
            return fruits[rf]


food()
