
import time as t
from _thread import *
from chat import Chat


class Runda(object):
    def __init__(self, haslo, rysujacy, gra):
        
        self.haslo = haslo
        self.rysujacy = rysujacy
        self.gracz_zgadujacy = []
        self.gracze_pomijajacy = []
        self.liczba_pominiec = 0
        self.czas = 75 #czas trfania rundy
        self.gra = gra
        self.wyniki_gracza = {gracz: 0 for gracz in self.gra.gracze}
        self.chat = Chat(self)
        start_new_thread(self.czas_thread, ()) #uruchomienie nowego wątki

    def pomin(self, gracz):
        
        if gracz not in self.gracze_pomijajacy:
            self.gracze_pomijajacy.append(gracz)
            self.liczba_pominiec += 1
            self.chat.update_chat(f"Głosowanie za pominieciem rundy ({self.liczba_pominiec}/{len(self.gra.gracze) -2})")
            if self.liczba_pominiec >= len(self.gra.gracze) - 2:
                return True

        return False

    def get_wyniki(self):
       
        return self.wyniki_gracza

    def get_wynik(self, gracz):
       
        if gracz in self.wyniki_gracza:
            return self.wyniki_gracza[gracz]
        else:
            raise Exception("Gracz nie figuruje w tablicy wynikow")

    def czas_thread(self):
       
        while self.czas > 0:
            t.sleep(1)
            self.czas -= 1
        self.koniec_rundy("Skończył się czas")

    def zgadywanie(self, gracz, wrd):
       
        poprawna_odpowiedz = wrd.lower() == self.haslo.lower()
        if poprawna_odpowiedz:
            self.chat.update_chat("Odgadnieto haslo")
            t.sleep(1)
            gracz.update_wynik(1)
            gracz.get_wynik()
            self.koniec_rundy("Odgadnięto haslo")
        else:
            self.chat.update_chat(f"{gracz.nazwa} :  {wrd}")


    def rozlaczenie(self, gracz):
       
        if gracz in self.wyniki_gracza:
            del self.wyniki_gracza[gracz]

        if gracz in self.gracz_zgadujacy:
            self.gracz_zgadujacy.remove(gracz)

        if gracz == self.rysujacy:
            self.chat.update_chat("Rysujacy gracz opuścił grę")
            self.koniec_rundy("Rysujacy gracz opuścił grę")

    def koniec_rundy(self, msg):
        for gracz in self.gra.gracze:
            if gracz in self.wyniki_gracza:
                gracz.update_wynik(self.wyniki_gracza[gracz])
        self.gra.koniec_rundy()

