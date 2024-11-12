from IkeaItem import IkeaItem
from MeasureableIkeaItem import MeasureableIkeaItem

class Lack(IkeaItem, MeasureableIkeaItem):
    def __init__(self, shelf_number, aisle_letter, name, price, color, height, width, length):
        IkeaItem.__init__(self, shelf_number, aisle_letter, name, price)
        MeasureableIkeaItem.__init__(self, height, width, length)
        self.color = color