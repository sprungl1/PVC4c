import re
class Bottle:
    def __init__(self, capacity_liters):
        self.capacity_liters = capacity_liters
        self.volume_liters = 0
        self.closed = True

    def open(self):
        self.closed = False

    def close(self):
        self.closed = True

    def set_volume_liters(self, volume_liters):
        if self.closed:
            raise Exception("Bottle is closed")
        else:
            if isinstance(volume_liters, int):
                if volume_liters > self.capacity_liters:
                    self.volume_liters = self.capacity_liters
                else:
                    self.volume_liters = volume_liters
            else:
                raise Exception("Volume liters not valid")


    def get_volume_liters(self):
        return self.volume_liters

    def set_volume_milliliters(self, volume_milliliters):
        if self.closed:
            raise Exception("Cannot change volume, the bottle is closed!")
        else:
            if isinstance(volume_milliliters, int):
                volume_liters = volume_milliliters / 1000
                if volume_liters > self.capacity_liters:
                    self.volume_liters = self.capacity_liters
                else:
                    self.volume_liters = volume_liters
            else:
                raise Exception("Volume milliliters not valid")

    def get_volume_milliliters(self):
        return self.volume_liters * 1000

    def empty(self):
        if self.closed:
            raise Exception("Cannot empty the bottle, it is closed!")
        else:
            self.volume_liters = 0





mojeLahev = Bottle(-100)
mojeLahev.open()
mojeLahev.set_volume_liters("AA")






