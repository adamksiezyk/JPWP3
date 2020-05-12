
from tablica import Tablica
from runda import Runda
import random


class Gra(object):

    def __init__(self, id, gracze):

        self.id = id
        self.gracze = gracze
        self.uzyte_hasla = set() #stworzenie pustego zbioru
        self.runda = None # None - obiekt pusty, zaznaczeni, że wartość jest dostępna, ale póki co nie jest określona
        self.tablica = Tablica()
        self.rysujacy_id = 0
        self.liczba_rund = 1
        self.nowa_runda() # wywołanie funkcji nowa_runda

    def nowa_runda(self):
        # Przy każdej rundzie wartość licznika rund oraz indeks gracza rysującego zostanie zinkrementowany, dzięki czemu będzie wiadomo kiedy odbyły
        #sie wszystkie kolejki i należy już zakończyć grę
        try:
            self.runda = Runda(self.get_haslo(), self.gracze[self.rysujacy_id], self)
            self.liczba_rund += 1

            if self.rysujacy_id >= len(self.gracze):
                self.koniec_rundy()
                self.koniec_gry()

            self.rysujacy_id += 1
        except Exception as e:
            self.koniec_gry()

    def proba_zgadniecia(self, gracz, haslo):

        return self.runda.zgadywanie(gracz, haslo)



    def get_wyniki_gracza(self):

        wyniki = {gracz.nazwa:gracz.get_wynik() for gracz in self.gracze}
        return wyniki

    def pomin(self, gracz):

        if self.runda:
            nowa_runda = self.runda.pomin(gracz)
            if nowa_runda:
                self.runda.chat.update_chat("Pominięto rundę")
                self.koniec_rundy()
                return True
            return False
        else:
            raise Exception("Runda jeszcze nie została rozpoczęta")

    def koniec_rundy(self):

        self.runda.chat.update_chat(f"Runda {self.liczba_rund} została zakończona.")
        self.nowa_runda()
        self.tablica.czyszczenie()

    def update_tablica(self, x, y, kolor):


        if not self.tablica:
            raise Exception("Nie utworzono tablicy")
        self.tablica.update(x,y,kolor)

    def koniec_gry(self):

        print(f" Gra {self.id} skończyła się")
        for gracz in self.gracze:
            gracz.gra = None

    def get_haslo(self):

        with open("hasla.txt", "r") as f:
            hasla = []

            for line in f:
                haslo = line.strip()
                if haslo not in self.uzyte_hasla:
                    hasla.append(haslo)

        haslo = random.choice(hasla)
        self.uzyte_hasla.add(haslo)

        return haslo
