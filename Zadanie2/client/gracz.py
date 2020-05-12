class Gracz(object):
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.wynik = 0

    def get_nazwa(self):
        return self.nazwa

    def ustaw_wynik(self, x):
        self.wynik = x