from ZvysitelnaUrovenInterface import ZvysitelnaUrovenInterface

class Mag(ZvysitelnaUrovenInterface):
    def __init__(self, bilaMagie, cernaMagie):
        if type(bilaMagie) is not bool:
            raise Exception("Bila magie musi byt True/False")
        if type(cernaMagie) is not bool:
            raise Exception("Cerna magie musi byt True/False")
        self.cernaMagie = cernaMagie
        self.bilaMagie = bilaMagie

    def zvysitUroven(self):
        if not self.bilaMagie:
            self.bilaMagie = True
        elif not self.cernaMagie:
            self.cernaMagie = True