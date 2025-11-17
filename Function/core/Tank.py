import pygame
import math

from PIL import Image

class Tank:  # Classe pour représenter le tank
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vitesse = 2  # Vitesse de déplacement du tank
        self.direction = 0

        Taille = 4
        Path = 'Images/Tank.png'
        # Ouvrir l'image
        Background_image = Image.open(Path)

        # Récupérer largeur et hauteur
        width, height = Background_image.size

        self.Tank = pygame.transform.scale(
            pygame.image.load(Path),
            (width * Taille, height * Taille)
        )

    def update(self, keys):
        if keys[pygame.K_d]:  # Avancer
            self.x += self.vitesse
            self.direction = 1
        elif keys[pygame.K_q]:  # Reculer
            self.x -= self.vitesse
            self.direction = -1
        else:
            self.direction = 0

    def draw(self, screen, angle):  # Dessiner le char
        screen.blit(self.Tank, (self.x, self.y))
        cannon_longueur = 40  # Longueur du canon
        cannon_start = (self.x + 9 * 4, self.y - 60)  # Point de départ du canon
        cannon_end_x = cannon_start[0] + cannon_longueur * math.cos(math.radians(angle))
        cannon_end_y = cannon_start[1] - cannon_longueur * math.sin(math.radians(angle))
        pygame.draw.line(screen, (255, 0, 0), cannon_start, (cannon_end_x, cannon_end_y), 5)  # Dessiner le canon
        return cannon_end_x, cannon_end_y  # Retourner la position de l'extrémité du canon
