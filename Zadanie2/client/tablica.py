#!
import pygame
import random

class Tablica:
    WIERSZE = KOLUMNY = 60
    KOLORY = {
        0: (255,255,255),
        1: (0,0,0),
    }

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.SZEROKOSC = 480
        self.WYSOKOSC = 480
        self.podzielona_tablica = []
        self.tablica = self.stworz_tablice()
        self.OBRAMOWANIE = 5
        print(self.x, self.y)
    def stworz_tablice(self):
        return [[(255,255,255) for _ in range(self.KOLUMNY)] for _ in range(self.WIERSZE)]

    def dzielenie_tablicy(self):
        for y, _ in enumerate(self.podzielona_tablica):
            for x, kol in enumerate(self.podzielona_tablica[y]):
                self.tablica[y][x] = self.KOLORY[kol]

    def rysuj(self, win):
        pygame.draw.rect(win, (0, 0, 0), (
        self.x - self.OBRAMOWANIE / 2, self.y - self.OBRAMOWANIE / 2, self.SZEROKOSC + self.OBRAMOWANIE, self.WYSOKOSC + self.OBRAMOWANIE), self.OBRAMOWANIE)
        for y, _ in enumerate(self.tablica):
            for x, kol in enumerate(self.tablica[y]):
                pygame.draw.rect(win, kol, (self.x + x*8, self.y + y*8, 8, 8), 0)

    def klikniecie(self,x,y):
      
        wiersze = int((x - self.x)/8)
        kolumny = int((y - self.y)/8)

        if 0 <= wiersze <= self.WIERSZE and 0 <= kolumny <= self.KOLUMNY:
            return wiersze, kolumny

        return None



    def update(self, x, y, kolor, thickness=3):
        sasiedzi = [(x, y)]
        for x, y in sasiedzi:
            if 0 <= x < self.KOLUMNY and 0 <= y < self.WIERSZE:
                self.tablica[y][x] = kolor

    def czyszczenie(self):
        self.tablica = self.stworz_tablice()
