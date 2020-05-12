class Gracz(object):
    def __init__(self, ip, nazwa):

        self.gra = None
        self.ip = ip
        self.nazwa = nazwa
        self.wynik = 0

    def zacznij_gre(self, gra):
        self.gra = gra

    def update_wynik(self, x):
        self.wynik += x

    def zgadnij(self, haslo):
        return self.gra.proba_zgadniecia(self,haslo)

    def rozlacz(self):
        self.gra.rozlaczony_gracz(self)

    def get_ip(self):
           return self.ip

    def get_nazwa(self):
         return self.nazwa

    def get_wynik(self):
        return self.wynik
