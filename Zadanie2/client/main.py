#OK
import pygame
from obsluga_klienta import Siec
from gra import Gra
from gracz import Gracz
from przyciski import Przycisk,PrzyciskTekstowy

class MainMenu:
    TLO = (255,255,255)
    def __init__(self):
        self.SZEROKOSC = 1090
        self.WYSOKOSC = 800
        self.win = pygame.display.set_mode((self.SZEROKOSC, self.WYSOKOSC))
        self.nazwa = ""
        self.oczekiwanie = False
        self.cznionka_nazwy = pygame.font.SysFont("comicsans", 80)
        self.czcionka_tytulu = pygame.font.SysFont("comicsans", 120)
        self.czcionka_enter = pygame.font.SysFont("comicsans", 60)
    def draw(self):
        self.win.fill(self.TLO)

        tytul = self.czcionka_tytulu.render("Kalambury!", 1, (0,0,0))
        self.win.blit(tytul, (self.SZEROKOSC/2 - tytul.get_width()/2, 50))

        nazwa = self.cznionka_nazwy.render("Podaj swój nick: " + self.nazwa, 1, (0,0,0))
        self.win.blit(nazwa, (100, 400))

        if self.oczekiwanie:
            enter = self.czcionka_enter.render("Oczekiwanie na graczy...", 1, (0, 0, 0))
            self.win.blit(enter, (self.SZEROKOSC / 2 - tytul.get_width() / 2, 600))
        else:
            enter = self.czcionka_enter.render("Naciśnij enter, aby dołączyć do gry...", 1, (0, 0, 0))
            self.win.blit(enter, (100, 600))

        pygame.display.update()

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(30)
            self.draw()
            if self.oczekiwanie:
                odpowiedz = self.n.send({-1:[]})
                if odpowiedz:
                    run = False
                    g = Gra(self.win, self.n)

                    for gracz in odpowiedz:
                        p = Gracz(gracz)
                        g.dodaj_gracza(p)
                    g.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if len(self.nazwa) > 1:
                            self.oczekiwanie = True
                            self.n = Siec(self.nazwa)
                    else:

                        key_name = pygame.key.name(event.key)


                        key_name = key_name.lower()
                        self.type(key_name)

    def type(self, znak):
        if znak == "backspace":
            if len(self.nazwa) > 0:
                self.nazwa = self.nazwa[:-1]
        elif znak == "space":
            self.nazwa += " "
        elif len(znak) == 1:
            self.nazwa += znak

        if len(self.nazwa) >= 20:
            self.nazwa = self.nazwa[:20]


if __name__ == "__main__":
    pygame.font.init()
    main = MainMenu()
    main.run()
