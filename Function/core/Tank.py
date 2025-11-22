import pygame
import math
from PIL import Image
import numpy as np

class Tank:
    def __init__(self, width, height, x, color_tank):
        self.x = x
        self.y = 540
        self.z_rotation = 0

        self.vitesse = 2
        self.direction = 0
        self.puissance = 10
        self.color = color_tank
        self.touche = False
        self.hp = 3
        self.can_shoot = True


        # chemin de l'image
        self.path = f"Images/Tank.png"  # ex: Tank_red.png

        # --- PIL image pour hitbox pixel-perfect ---
        self.image_pil = Image.open(self.path).convert("RGBA")
        self.pixels = self.image_pil.load()
        self.width, self.height = self.image_pil.size

        # --- Pygame image pour affichage ---
        Taille = 4
        self.image_pg = pygame.transform.scale(
            pygame.image.load(self.path),
            (self.width * Taille, self.height * Taille)
        )

        # Nouveaux width/height après le scale pygame
        self.draw_width = self.width * Taille
        self.draw_height = self.height * Taille

        self.Base_draw_width = self.draw_width
        self.Base_draw_height = self.draw_height

        # Angle de base (vise le centre de l'écran)
        dx = (width / 2) - (self.x + self.draw_width / 2)
        dy = (height * 0.75) - self.y
        self.angle = math.degrees(math.atan2(-dy, dx))  # CORRIGÉ


    # --- Hitbox Pixel-Perfect PIL ---
    def hit(self, balle):
        bx = int((balle.x - self.x) / 4)
        by = int((balle.y - self.y) / 4)

        if 0 <= bx < self.width and 0 <= by < self.height:
                r, g, b, a = self.pixels[bx, by]
                if a > 10:
                    return True   # une seule détection par balle
        return False


    # --- Affichage du tank ---
    def draw(self, screen, array_terrain):
        self.x = int(self.x)
        self.y = int(array_terrain[self.x])

        # Angle de base (vise le centre de l'écran)
        dx = self.draw_width
        x_index_by_y = self.x + self.draw_width
        dy = int(array_terrain[int(x_index_by_y)]) - self.y
        self.z_rotation = math.degrees(math.atan2(-dy, dx))

        image_pg_temp = pygame.transform.rotate(self.image_pg, self.z_rotation)
        self.draw_width, self.draw_height = image_pg_temp.get_size()
        print(self.z_rotation)
        if self.z_rotation > 0:
            caca = (self.z_rotation / 90) * 25
            screen.blit(image_pg_temp, (self.x, (self.y - self.draw_height - caca)))
        else:
            caca = (self.z_rotation / 90) * 25
            screen.blit(image_pg_temp, (self.x, (self.y - self.Base_draw_height - caca)))

        # Position canon
        cannon_length = 40
        cannon_start = (self.x + self.draw_width / 2 - 2.5, self.y + 10)

        cannon_end_x = cannon_start[0] + cannon_length * math.cos(math.radians(self.angle))
        cannon_end_y = cannon_start[1] - cannon_length * math.sin(math.radians(self.angle))

        pygame.draw.line(screen, (0, 100, 0), cannon_start, (cannon_end_x, cannon_end_y), 5)

        return cannon_end_x, cannon_end_y
