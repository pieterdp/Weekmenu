from datetime import datetime
from menu.exceptions import InvalidParameterException
from menu.storage.models.ingredient import Ingredient
from menu.storage.models import Model


class Recipe(Model):

    seasons = {
        '1': 'Winter',
        '2': 'Spring',
        '3': 'Summer',
        '4': 'Autumn'
    }

    def __init__(self, name, date=None, recipe=None, recipe_link=None, ingredients=(), season=None):
        self.name = name
        self.date = date
        if not date:
            self.date = datetime.now()
        if not recipe and not recipe_link:
            raise InvalidParameterException('Either the full recipe or a link must be provided.')
        self.recipe = recipe
        self.recipe_link = recipe_link
        self.ingredients = []
        for ingredient in ingredients:
            if type(ingredient) != Ingredient:
                self.ingredients.append(Ingredient(**ingredient))
            else:
                self.ingredients.append(ingredient)
        self.season = season
        if not season:
            self.season = self.__season()

    def to_db(self):
        pass

    def from_db(self):
        pass

    def __season(self):
        # https://stackoverflow.com/questions/44124436/python-datetime-to-season/44124490
        season_n = (self.date.month % 12 + 3) // 3
        return self.seasons[str(season_n)]
