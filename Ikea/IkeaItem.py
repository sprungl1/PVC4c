class IkeaItem:
    def __init__(self, shelf_number, aisle_letter, name, price):
        if not (1 <= shelf_number <= 100):
            raise ValueError("Shelf number must be between 1 and 100.")
        if aisle_letter not in "ABCDEFGHIJK":
            raise ValueError("Aisle letter must be between A and K.")
        self.shelf_number = shelf_number
        self.aisle_letter = aisle_letter
        self.name = name
        self.price = price