from menu.exceptions import InvalidParameterException
from menu.storage.models import Model


class Ingredient(Model):

    def __init__(self, name, quantity=None):
        self.name = name
        self.quantity = quantity

    def to_db(self):
        pass

    def from_db(self):
        pass
