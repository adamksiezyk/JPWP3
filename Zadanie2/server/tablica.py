
class Tablica(object):
    WIERSZE = KOLUMNY = 60 # Tablica dzielona jest na małe kwadraty, tak aby umożliwić rysowanie

    def __init__(self):

        self.dane = self.pusta_tablica()

    def update(self, x, y, kolor):

        podzial = [(x, y)]
        for x, y in podzial:
            if 0 < x < self.KOLUMNY and 0 < y < self.WIERSZE:
                self.dane[y][x] = kolor

    def czyszczenie(self):

        self.dane = self.pusta_tablica()

    def pusta_tablica(self):

        return [[0 for _ in range(self.KOLUMNY)] for _ in range(self.WIERSZE)]

    def get_tablica(self):

        return self.dane
