import pygame
import random


class Particule:  # Classe pour représenter une particule
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.lifetime = random.uniform(0, 150)  # Durée de vie de la particule
        self.gravité = 0.1  # Gravité initiale
        self.rayon = random.uniform(0, 4)

    def update(self):
        self.x += self.vx
        self.y += self.vy + self.gravité  # Appliquer la gravité
        self.gravité += 0.03  # Augmenter la gravité à chaque mise à jour
        self.lifetime -= 1
        self.rayon -= 0.015

    def draw(self, screen):
        if self.lifetime > 0:
            pygame.draw.circle(screen, (0, 100, 0), (int(self.x), int(self.y)), int(self.rayon))