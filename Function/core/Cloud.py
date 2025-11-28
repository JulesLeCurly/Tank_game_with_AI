import pygame
import random

class Cloud:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        # position aléatoire
        self.x = random.randint(0, screen_width)
        self.y = random.randint(20, 200)

        # taille aléatoire
        self.width = random.randint(80, 180)
        self.height = random.randint(40, 90)

        # vitesse aléatoire
        self.speed = random.uniform(0.2, 1.2)

        # couleur (blanc léger)
        self.color = (255, 255, 255, 200)

    def update(self):
        self.x -= self.speed

        # Si le nuage sort de l'écran → on le remet à droite
        if self.x + self.width < 0:
            self.x = self.screen_width + random.randint(20, 100)
            self.y = random.randint(20, 200)
            self.width = random.randint(80, 180)
            self.height = random.randint(40, 90)
            self.speed = random.uniform(0.2, 1.2)

    def draw(self, screen):
        # Plusieurs ellipses pour un effet de nuage "fluffy"
        pygame.draw.ellipse(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
        pygame.draw.ellipse(screen, (255, 255, 255), (self.x + 30, self.y - 10, self.width * 0.8, self.height * 0.8))
        pygame.draw.ellipse(screen, (255, 255, 255), (self.x + 50, self.y + 15, self.width * 0.7, self.height * 0.7))
