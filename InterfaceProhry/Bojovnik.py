from ZvysitelnaUrovenInterface import ZvysitelnaUrovenInterface

class Bojovnik(ZvysitelnaUrovenInterface):
    def __init__(self, sila):
        if type(sila) is not int or sila < 0 or sila > 3:
            raise Exception("Sila bojovnika neni dostatecne dlouhe")
        self.sila = sila

    def zvysitUroven(self):
        if self.sila < 3:
            self.sila += 1