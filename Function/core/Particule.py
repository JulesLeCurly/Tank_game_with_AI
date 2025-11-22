import pygame
import random

# Couleurs des particules
coco = {
    "red":  (140, 0, 0),
    "blue": (0, 0, 140)
}


class Particule:
    """Particule d'explosion avec gravité et durée de vie."""

    def __init__(self, x, y, color):

        # Position initiale
        self.x = x
        self.y = y

        # Vitesse aléatoire
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)

        # Gravité progressive
        self.gravite = 0.1

        # Durée de vie
        self.lifetime = random.uniform(0, 150)

        # Rayon initial
        self.rayon = random.uniform(0, 4)

        # Couleur (red ou blue)
        self.color = color


    # ================================================================
    # 🔵 Mise à jour (physique + réduction du rayon + durée)
    # ================================================================
    def update(self):
        self.x += self.vx
        self.y += self.vy + self.gravite

        # Gravité augmente au fil du temps
        self.gravite += 0.03

        # La particule vit moins longtemps
        self.lifetime -= 1

        # Réduction du rayon -> effet d'effacement progressif
        self.rayon -= 0.015


    # ================================================================
    # 🔵 Affichage
    # ================================================================
    def draw(self, screen):
        if self.lifetime > 0 and self.rayon > 0:
            pygame.draw.circle(
                screen,
                coco[self.color],
                (int(self.x), int(self.y)),
                int(self.rayon)
            )
