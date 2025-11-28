import pygame
import math
from PIL import Image
import numpy as np

# Couleurs du canon
cocotank = {
    "red":  (100, 0, 0),
    "blue": (0, 0, 100)
}

class Tank:
    def __init__(self, width, height, x, color_tank):

        # Position
        self.x = x
        self.y = 540
        self.z_rotation = 0

        # Stats
        self.vitesse = 2
        self.direction = 0
        self.puissance = 10
        self.color = color_tank
        self.touche = False
        self.hp = 3
        self.can_shoot = True

        # ----- IMAGE SOURCE -----
        self.path = f"Images/Tank_{color_tank}.png"  # ex : Images/Tank_red.png

        # ----- PIL pour HITBOX PIXEL PERFECT -----
        self.image_pil = Image.open(self.path).convert("RGBA")
        self.pixels = self.image_pil.load()
        self.width, self.height = self.image_pil.size

        # ----- Pygame pour AFFICHAGE -----
        Taille = 4
        self.image_pg = pygame.transform.scale(
            pygame.image.load(self.path),
            (self.width * Taille, self.height * Taille)
        )

        self.draw_width  = self.width  * Taille
        self.draw_height = self.height * Taille

        self.Base_draw_width  = self.draw_width
        self.Base_draw_height = self.draw_height

        # ----- ANGLE INITIAL (vise le centre écran) -----
        dx = (width / 2) - (self.x + self.draw_width / 2)
        dy = (height * 0.75) - self.y
        self.angle = math.degrees(math.atan2(-dy, dx))


    # ====================================================
    # 🔥 HITBOX PIXEL-PERFECT
    # ====================================================
    def hit(self, balle):

        # Centre de rotation (même centre que pour pygame.transform.rotate)
        cx = self.x + self.draw_width  / 2
        cy = self.y - (self.draw_height / 2)

        # Coordonnées balle relatives au centre
        dx = balle.x - cx
        dy = balle.y - cy

        # Rotation inverse
        angle_rad = math.radians(self.z_rotation)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)

        # rotation inverse : (x', y') = rot(-angle) * (dx, dy)
        rx =  dx * cos_a + dy * sin_a
        ry = -dx * sin_a + dy * cos_a

        # Revenir dans le repère de l’image non-rotée
        bx = int((rx + self.Base_draw_width/2)  / 4)
        by = int((ry + self.Base_draw_height/2) / 4)

        # Test pixel-perfect
        if 0 <= bx < self.width and 0 <= by < self.height:
            r, g, b, a = self.pixels[bx, by]
            if a > 0:  # pixel non transparent
                return True

        return False


    # ====================================================
    # 🔥 DESSIN DU TANK + ANGLE DU SOL + CANON
    # ====================================================
    def draw(self, screen, array_terrain):

        self.x = int(self.x)
        self.y = int(array_terrain[self.x])

        # ----- Angle Tank selon le terrain -----
        dx = self.draw_width
        x_index_by_y = self.x + self.draw_width

        dy = int(array_terrain[int(x_index_by_y)]) - self.y
        self.z_rotation = math.degrees(math.atan2(-dy, dx))

        # Rotation Pygame
        image_pg_temp = pygame.transform.rotate(self.image_pg, self.z_rotation)
        self.draw_width, self.draw_height = image_pg_temp.get_size()

        # Correction hauteur selon angle (le fameux "caca")
        caca = (self.z_rotation / 90) * 25

        if self.z_rotation > 0:
            y = (self.y - self.draw_height - caca)
        else:
            y = (self.y - self.Base_draw_height - caca)

        # Dessin
        screen.blit(image_pg_temp, (self.x, y))

        # ----- Calcul du bout du canon -----
        cannon_length = 40
        cannon_start = [self.x + self.draw_width / 2, y + self.draw_height / 2]

        cannon_start[0] += (20 * math.cos(math.radians(self.angle) + math.radians(self.z_rotation))) # rotation attached to tank
        cannon_start[1] -= (20 * math.sin(math.radians(self.angle) + math.radians(self.z_rotation))) # rotation attached to tank

        cannon_end_x = cannon_start[0] + cannon_length * math.cos(math.radians(self.angle) + math.radians(self.z_rotation))
        cannon_end_y = cannon_start[1] - cannon_length * math.sin(math.radians(self.angle) + math.radians(self.z_rotation))

        # Dessin du canon
        pygame.draw.line(
            screen,
            cocotank[self.color],
            cannon_start,
            (cannon_end_x, cannon_end_y),
            5
        )

        return cannon_end_x, cannon_end_y
