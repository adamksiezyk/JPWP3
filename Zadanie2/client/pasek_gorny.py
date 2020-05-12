#ok!
import pygame


class PasekGorny(object):
    def __init__(self, x, y, szerokosc, wysokosc):
        self.x = x
        self.y = y
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.haslo = ""
        self.runda = 1
        self.max_rund = 8
        self.czcinka_licznika_rund = pygame.font.SysFont("comicsans", 50)
        self.OBRAMOWANIE = 5
        self.czas = 75
        self.rysujacy = False

    def rysuj(self, win):
        pygame.draw.rect(win, (139, 0, 0), (self.x ,self.y, self.szerokosc, self.wysokosc), self.OBRAMOWANIE)
        pygame.draw.rect(win, (139, 0, 0), (self.x+2.5, self.y+2.5, self.szerokosc-5, self.wysokosc-5))

        if self.runda != []:
             txt = self.czcinka_licznika_rund.render(f"Runda {self.runda} / {self.max_rund}", 1, (0,0,0))
             win.blit(txt, (self.x + 10, self.y + self.wysokosc/2 - txt.get_height()/2))
        else:
            txt = self.czcinka_licznika_rund.render("Koniec gry", 1, (0, 0, 0))
            win.blit(txt, (self.x + 10, self.y + self.wysokosc / 2 - txt.get_height() / 2))


        if self.rysujacy:
            wrd = self.haslo
        else:
            wrd = PasekGorny.podkreslony_tekst(self.haslo)
        txt = self.czcinka_licznika_rund.render(wrd, 1, (0,0,0))
        win.blit(txt, (self.x + self.szerokosc/2 - txt.get_width()/2, self.y + self.wysokosc/2 - txt.get_height()/2 + 10))

        pygame.draw.circle(win, (0,0,0), (self.x + self.szerokosc - 50, self.y + round(self.wysokosc/2)), 40,self.OBRAMOWANIE)
        licznik_czasu = self.czcinka_licznika_rund.render(str(self.czas), 1, (0,0,0))
        win.blit(licznik_czasu, (self.x + self.szerokosc - 50 - licznik_czasu.get_width()/2, self.y + self.wysokosc/2 - licznik_czasu.get_height()/2))

    @staticmethod
    def podkreslony_tekst(text):
        nowy_napis = ""

        for znak in text:
            if znak != " ":
                nowy_napis += " _ "
            else:
                nowy_napis += "   "

        return nowy_napis

    def zmiana_slowa(self, haslo):
        self.haslo = haslo

    def zmiana_rundy(self, rnd):
        self.runda = rnd
