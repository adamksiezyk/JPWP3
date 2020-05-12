#ok
import pygame


class Ranking(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.SZEROKOSC = 230
        self.WYSOKOSC_PASKA = 80
        self.gracze = []
        self.czcionka_gracze = pygame.font.SysFont("comicsans", 25,bold=True)
        self.czcionka_wynik = pygame.font.SysFont("comicsans", 20)
        self.czcionka_ranking = pygame.font.SysFont("comicsans", 60)
        self.OBRAMOWANIE = 5

    def rysuj(self, win):
        wyniki = [(gracz.nazwa, gracz.wynik) for gracz in self.gracze]
        wyniki.sort(key=lambda x: x[1], reverse=True)

        for i, wynik in enumerate(wyniki):
          
            kolor = (200,200,200)
            pygame.draw.rect(win,kolor ,(self.x, self.y + i*self.WYSOKOSC_PASKA, self.SZEROKOSC, self.WYSOKOSC_PASKA))

    
            rank = self.czcionka_ranking.render( str(i+1), 1, (0,0,0))
            win.blit(rank, (self.x + 10, self.y + i*self.WYSOKOSC_PASKA + self.WYSOKOSC_PASKA/2 - rank.get_height()/2))

            nazwa = self.czcionka_gracze.render(wynik[0], 1, (0,0,0))
            win.blit(nazwa, (self.x - nazwa.get_width()/2 + self.SZEROKOSC/2, self.y + i*self.WYSOKOSC_PASKA + 20))

            wynik = self.czcionka_wynik.render("Wynik: " + str(wynik[1]), 1, (0, 0, 0))
            win.blit(wynik, (self.x - nazwa.get_width() / 2 + self.SZEROKOSC / 2, self.y + i * self.WYSOKOSC_PASKA + 40))

        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.SZEROKOSC, self.WYSOKOSC_PASKA * len(wyniki)),
                         self.OBRAMOWANIE)

    def dodaj_gracza(self, gracz):
        self.gracze.append(gracz)

    def usun_gracza(self, gracz):
        self.gracze.remove(gracz)
