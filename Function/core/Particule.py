import pygame
import random
coco={"red":(255,0,0), "blue":(0,0,255)}

class Particule:  # Classe pour représenter une particule
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.lifetime = random.uniform(0, 150)  # Durée de vie de la particule
        self.gravité = 0.1  # Gravité initiale
        self.rayon = random.uniform(0, 4)
        self.color = color

    def update(self):
        self.x += self.vx
        self.y += self.vy + self.gravité  # Appliquer la gravité
        self.gravité += 0.03  # Augmenter la gravité à chaque mise à jour
        self.lifetime -= 1
        self.rayon -= 0.015

    def draw(self, screen):
        if self.lifetime > 0:
            pygame.draw.circle(screen, coco[self.color], (int(self.x), int(self.y)), int(self.rayon))