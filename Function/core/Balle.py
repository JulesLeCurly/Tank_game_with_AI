import pygame
import random
import math

class Balle:   # Classe pour représenter la balle
    def __init__(self, screen_width, screen_height, x, y, rayon, angle, vitesse, vitesse_tank, owner):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rayon = rayon
        self.x = x
        self.y = y
        self.gravité = 0.5
        self.angle_rad = math.radians(angle)
        self.Vitesse_x = vitesse * math.cos(self.angle_rad) + vitesse_tank
        self.Vitesse_y = -vitesse * math.sin(self.angle_rad)  # Négatif car l'axe Y est inversé
        self.visible = True
        self.rayon = rayon
        self.owner = owner   # tank qui tire


    def update(self):
        if self.visible:
            self.x += self.Vitesse_x
            self.y += self.Vitesse_y
            self.Vitesse_y += self.gravité
            if self.x < -self.rayon or self.x > self.screen_width + self.rayon or self.y > 595 or self.y > self.screen_height + self.rayon:  # Vérifier si la balle dépasse les bords de la fenêtre
                self.visible = False  # La balle disparaît
                return (self.x, self.y)  # Retourner la position de la balle avant de disparaître
        return None

    def draw(self, screen):
        if self.visible:
            pygame.draw.circle(screen, (0, 100, 0), (int(self.x), int(self.y)), self.rayon)
