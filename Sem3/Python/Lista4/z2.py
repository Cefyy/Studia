class Formula:
    def __init__(self):
        pass
    def oblicz(self,zmienne):
        pass
    def __add__(self,other):
        return self or other
    def __mult__(self,other):
        return self and other
    def tautologia(self):
        import itertools
        zmienne = sorted(self._zbierz_zmienne)

class And(Formula):
    pass
class Or(Formula):
    pass
class Zmienna(Formula):
    


    