

class Recipe:

    def __init__(self, name, recipe, ingredients=(), rating=None):
        self.__recipe = {}
        self.name = name
        self.recipe = recipe
        self.ingredients = ingredients
        self.rating = rating

    def __mk(self):
        self.__recipe['name'] = self.name
        self.__recipe['recipe'] = self.recipe
        self.__recipe['ingredients'] = self.ingredients
        self.__recipe['rating'] = self.rating

    def db_obj(self):
        self.__mk()
        return self.__recipe

    def api_obj(self):
        self.__mk()
        return self.__recipe
