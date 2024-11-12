# SamlaBox.py
from IkeaItem import IkeaItem
from MeasureableIkeaItem import MeasureableIkeaItem
from PlasticWasteIkeaItem import PlasticWasteIkeaItem

class SamlaBox(IkeaItem, MeasureableIkeaItem, PlasticWasteIkeaItem):
    def __init__(self, shelf_number, aisle_letter, name, price, volume, height, width, length, plastic_weight):
        IkeaItem.__init__(self, shelf_number, aisle_letter, name, price)
        MeasureableIkeaItem.__init__(self, height, width, length)
        PlasticWasteIkeaItem.__init__(self, plastic_weight)
        self.volume = volume