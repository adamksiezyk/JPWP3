import pygame
import math
import sys

#TODO zaimportuj moduł pygame i utwórz ekran (zmienna screen) o wymiarach 1200x600, ustaw także tytuł ekranu "JPWP-project"
screen = pygame.display.set_mode((1200, 600))
screen.set_caption("JPWP-project")
screen_CENTER = 600, 300

class Player(object):

    def __init__(self):
        self.x, self.y = screen_CENTER
        self.surface = pygame.image.load('player&hand.png')
        #TODO Skopiuj obrazek do zmiennej rotated_surface
        self.rotated_surface = self.surface
        self.rect = self.surface.get_rect()
        self.speed = 0.4

    def rotate(self, angle):
        self.rotated_surface = pygame.transform.rotate(self.surface, angle)
        self.rect = self.rotated_surface.get_rect(center=screen.get_rect().center)

    def draw(self):
        #TODO Uzupełnij funkcję blit
        screen.blit(self.surface, self.x, self.y)

player1 = Player()

running = True

def redraw():
    # TODO uzupełnij funkcję redraw w celu usunięcia efekty zostawiania "śladu" przy przesuwaniu graczem
    player1.draw()
    pygame.display.update()

while (running):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            #TODO ustaw wyłączanie gry za pomocą przycisku Esc
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                sys.exit()
            if keys[pygame.K_a]:
                player1.x -= player1.speed
            #TODO Dopisz kolejne ify sprawdzające czy czy użytkownik nacisnął klawisze: W, S, D oraz podaj instrukcje, które określają sposób poruszania się gracza
            if keys[pygame.K_w]:
                player1.y += player1.speed
            if keys[pygame.K_s]:
                player1.y -= player1.speed
            if keys[pygame.K_d]:
                player1.x += player1.speed

        elif e.type == pygame.MOUSEMOTION:

        #TODO Do zmiennych mouse_x i mouse_y przypisz aktualną pozycję kursora myszki. Określamy kąt pomiędzy odpowiednimi punktami (funkcja atan2), pamiętaj w jakich wartościach atan2 zwraca wynik
            mouse_x, mouse_y = pygame.mouse.get_pos()
            angle = atan2(mouse_y/mouse_x)
            angle = math.degrees(angle)
            angle += 180
            player1.rotate(angle)

    redraw()
pygame.quit()