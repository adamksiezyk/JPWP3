import pygame

class Chat:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.SZEROKOSC = 225
        self.WYSOKOSC = 350
        self.OBRAMOWANIE = 5
        self.chat_tablica = []
        self.pisanie = ""
        self.chat_czcionka = pygame.font.SysFont("comicsans", 20)
        self.pisanie_czcionka = pygame.font.SysFont("comicsans", 30)
        self.WPISYWANIE = 20

    def update_chat(self, chat_tablica):
        self.chat_tablica = chat_tablica

    def rysuj(self, win):
      #Rysowanie okienka czastu
        pygame.draw.line(win, (0,0,0), (self.x, self.y + self.WYSOKOSC - 40), (self.x + self.SZEROKOSC, self.y + self.WYSOKOSC - 40), self.OBRAMOWANIE)
        pygame.draw.rect(win, (0,0,0),(self.x, self.y, self.SZEROKOSC, self.WYSOKOSC) ,self.OBRAMOWANIE)
        #czcionka widoczna na czacie
        for i, chat in enumerate(self.chat_tablica):
            txt = self.chat_czcionka.render(" - " + chat, 1, (0,0,0))
            win.blit(txt, (self.x + 8, 10 + self.y + i*self.WPISYWANIE))
        #czcinka dla miejsca do wpisywania wiadomosci
        type_chat = self.pisanie_czcionka.render(self.pisanie, 1, (0,0,0))
        win.blit(type_chat, (self.x + 5, self.y+self.WYSOKOSC-17-type_chat.get_height()/2))

    def type(self, znak):
        #kasowanie
        if znak == "backspace":
            if len(self.pisanie) > 0:
                self.pisanie = self.pisanie[:-1]
        #spacja
        elif znak == "space":
            self.pisanie += " "
        #żeby wogóle zaczeło pisać
        elif len(znak) == 1:
            self.pisanie += znak
        #ograniczenie dlugosci  wpisywanej wiadomosci
        if len(self.pisanie) >= 15:
            self.pisanie = self.pisanie[:15]

