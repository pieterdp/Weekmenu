from datetime import datetime
import pytz


class Menu:

    def __init__(self, recipes, week=None, year=None):
        dt = datetime.now(tz=pytz.timezone('Europe/Brussels'))
        self.year = year
        if not year:
            self.year = dt.year
        self.week = week
        if not week:
            self.week = dt.strftime('%W')
        self.recipes = {}
        self.add_recipes(recipes)

    def add_recipes(self, recipes):
        if type(recipes) != type(dict):
            recipes = [recipes]
        for day, recipe in recipes.items():
            self.recipes[day] = recipe
