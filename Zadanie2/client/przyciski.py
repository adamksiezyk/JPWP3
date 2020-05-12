#ok!
import pygame


class Przycisk:

    def __init__(self, x, y, szerokosc, wysokosc, kolor, kolor_obramiwania=(0,0,0)):
        self.x = x
        self.y = y
        self.wysokosc = wysokosc
        self.szerokosc = szerokosc
        self.kolor = kolor
        self.kolor_obramiwania = kolor_obramiwania
        self.OBRAMOWANIE = 2

    def rysuj(self, win):
        pygame.draw.rect(win, self.kolor_obramiwania, (self.x, self.y, self.szerokosc, self.wysokosc), 0)
        pygame.draw.rect(win, self.kolor, (
        self.x + self.OBRAMOWANIE, self.y + self.OBRAMOWANIE, self.szerokosc - self.OBRAMOWANIE * 2,
        self.wysokosc - self.OBRAMOWANIE * 2), 0)

    def klikniecie(self, x, y):
      

        if self.x <= x <= self.x + self.szerokosc and self.y <= y <= self.y + self.wysokosc:
            return True  

        return False


class PrzyciskTekstowy(Przycisk):
    def __init__(self, x, y, szerokosc, wysokosc, kolor, tekst, kolor_obramiwania=(0,0,0)):
        super().__init__(x, y, szerokosc, wysokosc, kolor, kolor_obramiwania)
        self.tekst = tekst
        self.tekst_czcionka = pygame.font.SysFont("comicsans", 30)

    def zmaina_czcionki(self, size):
        self.tekst_czcionka = pygame.font.SysFont("comicsans", size)

    def rysuj(self, win):
        super().rysuj(win)
        txt = self.tekst_czcionka.render(self.tekst, 1, (0,0,0))
        win.blit(txt, (self.x + self.szerokosc/2 - txt.get_width()/2, self.y + self.wysokosc/2 - txt.get_height()/2))


