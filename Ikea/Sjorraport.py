# Sjorraport.py
from IkeaItem import IkeaItem
from PlasticWasteIkeaItem import PlasticWasteIkeaItem

class Sjorraport(IkeaItem, PlasticWasteIkeaItem):
    def __init__(self, shelf_number, aisle_letter, name, price, expiration, weight, plastic_weight):
        IkeaItem.__init__(self, shelf_number, aisle_letter, name, price)
        PlasticWasteIkeaItem.__init__(self, plastic_weight)
        self.expiration = expiration
        self.weight = weight