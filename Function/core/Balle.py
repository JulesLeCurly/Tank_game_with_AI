import pygame
import random
import math

# Couleurs des balles
coco = {
    "red":  (190, 0, 0),
    "blue": (0, 0, 190)
}


class Balle:
    """Représente un projectile tiré par un tank."""

    def __init__(self, screen_width, screen_height,
                 x, y, rayon, angle,
                 vitesse, vitesse_tank,
                 owner, color_tank):

        # Dimensions écran
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Position de départ
        self.x = x
        self.y = y
        self.rayon = rayon

        # Physique
        self.gravite = 0.5
        self.angle_rad = math.radians(angle)

        # Vitesse initiale + prise en compte du déplacement du tank tireur
        self.Vitesse_x = vitesse * math.cos(self.angle_rad) + vitesse_tank
        self.Vitesse_y = -vitesse * math.sin(self.angle_rad)  # Y inversé en Pygame

        # Propriétés
        self.visible = True
        self.owner = owner
        self.color = color_tank


    # ============================================================
    # 🔵 Mise à jour du projectile (gravité + mouvement + disparition)
    # ============================================================
    def update(self, terrain_array):
        if self.visible:

            # Déplacement
            self.x += self.Vitesse_x
            self.y += self.Vitesse_y

            # Gravité
            self.Vitesse_y += self.gravite

            # Suppression si hors écran
            if (
                self.x < -self.rayon or
                self.x > self.screen_width + self.rayon or
                self.y > 595 or
                self.y > self.screen_height + self.rayon
            ):
                self.visible = False
                # Retourne la dernière position valide pour tests de collision
                return (self.x, self.y)
            
            # Suppression si collision avec le terrain
            if 0 <= int(self.x) < self.screen_width:
                terrain_y = terrain_array[int(self.x)]
                if self.y + self.rayon >= terrain_y:
                    self.visible = False
                    return (self.x, self.y)

        return None


    # ============================================================
    # 🔵 Dessin du projectile
    # ============================================================
    def draw(self, screen):
        if self.visible:
            pygame.draw.circle(
                screen,
                coco[self.color],
                (int(self.x), int(self.y)),
                self.rayon
            )
