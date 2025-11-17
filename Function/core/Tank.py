import pygame
import math

class Tank:  # Classe pour représenter le tank
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vitesse = 2  # Vitesse de déplacement du tank
        self.direction = 0

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
        GREEN = (80, 170, 0)
        DARK_GREEN = (0, 100, 0)
        BROWN = (139, 69, 19)
        BLACK = (0, 0, 0)
        OLIVE = (128, 128, 0)
        YELLOW = (200, 200, 0)
        pygame.draw.rect(screen, BLACK, (self.x, self.y, 19 * 4, 1 * 4))  # Chenille basse
        pygame.draw.rect(screen, OLIVE, (self.x, self.y - 1 * 4, 19 * 4, 1 * 4))  # Chenille supérieure
        pygame.draw.rect(screen, BLACK, (self.x - 1 * 4, self.y - 1 * 4, 1 * 4, 1 * 4))
        pygame.draw.rect(screen, BLACK, (self.x + 19 * 4, self.y - 1 * 4, 1 * 4, 1 * 4))
        pygame.draw.rect(screen, BLACK, (self.x - 2 * 4, self.y - 2 * 4, 1 * 4, 1 * 4))
        pygame.draw.rect(screen, OLIVE, (self.x - 1 * 4, self.y - 2 * 4, 1 * 4, 1 * 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x, self.y - 2 * 4, 1 * 4, 1 * 4))
        pygame.draw.rect(screen, BLACK, (self.x + 1 * 4, self.y - 2 * 4, 1 * 4, 1 * 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 2 * 4, self.y - 2 * 4, 3 * 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 5 * 4, self.y - 2 * 4, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 6 * 4, self.y - 2 * 4, 3 * 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 9 * 4, self.y - 2 * 4, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 10 * 4, self.y - 2 * 4, 3 * 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 13 * 4, self.y - 2 * 4, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 14 * 4, self.y - 2 * 4, 3 * 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 17 * 4, self.y - 2 * 4, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 18 * 4, self.y - 2 * 4, 4, 4))
        pygame.draw.rect(screen, OLIVE, (self.x + 19 * 4, self.y - 2 * 4, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 80, self.y - 8, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x - 8, self.y - 16, 4, 12))
        pygame.draw.rect(screen, DARK_GREEN, (self.x - 4, self.y - 12, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x, self.y - 12, 4, 4))
        pygame.draw.rect(screen, YELLOW, (self.x + 4, self.y - 12, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 8, self.y - 12, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 12, self.y - 12, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 16, self.y - 12, 4, 4))
        pygame.draw.rect(screen, YELLOW, (self.x + 20, self.y - 12, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 6 * 4, self.y - 12, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 7 * 4, self.y - 12, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 8 * 4, self.y - 12, 4, 4))
        pygame.draw.rect(screen, YELLOW, (self.x + 9 * 4, self.y - 12, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 4, self.y - 4, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 11, self.y - 3, 1, 1))
        pygame.draw.rect(screen, BLACK, (self.x + 12 * 4, self.y - 12, 4, 4))
        pygame.draw.rect(screen, YELLOW, (self.x + 13 * 4, self.y - 12, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 14 * 4, self.y - 12, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 15 * 4, self.y - 12, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 16 * 4, self.y - 12, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 18 * 4, self.y - 12, 4, 4))
        pygame.draw.rect(screen, YELLOW, (self.x + 68, self.y - 12, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 76, self.y - 12, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 80, self.y - 16, 4, 8))
        pygame.draw.rect(screen, OLIVE, (self.x, self.y - 4, 76, 4))  # Chenille 2ème ligne
        pygame.draw.rect(screen, BLACK, (self.x - 4, self.y - 16, 4, 4))
        pygame.draw.rect(screen, OLIVE, (self.x + 76, self.y - 16, 4, 4))
        pygame.draw.rect(screen, OLIVE, (self.x - 4, self.y - 16, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x, self.y - 16, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 4, self.y - 16, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 8, self.y - 16, 12, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 20, self.y - 16, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 24, self.y - 16, 12, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 36, self.y - 16, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 40, self.y - 16, 12, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 52, self.y - 16, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 56, self.y - 16, 12, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 68, self.y - 16, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 72, self.y - 16, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x - 4, self.y - 20, 4, 4))
        pygame.draw.rect(screen, OLIVE, (self.x, self.y - 20, 76, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 76, self.y - 20, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x, self.y - 24, 76, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 8, self.y - 28, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 12, self.y - 28, 56, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 68, self.y - 28, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 12, self.y - 32, 56, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 12, self.y - 40, 4, 8))
        pygame.draw.rect(screen, GREEN, (self.x + 16, self.y - 40, 4, 8))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 20, self.y - 40, 32, 8))
        pygame.draw.rect(screen, GREEN, (self.x + 52, self.y - 40, 4, 8))
        pygame.draw.rect(screen, BLACK, (self.x + 56, self.y - 40, 4, 8))
        pygame.draw.rect(screen, BLACK, (self.x + 16, self.y - 48, 4, 8))
        pygame.draw.rect(screen, BLACK, (self.x + 52, self.y - 48, 4, 8))
        pygame.draw.rect(screen, GREEN, (self.x + 48, self.y - 48, 4, 8))
        pygame.draw.rect(screen, GREEN, (self.x + 20, self.y - 48, 4, 8))
        pygame.draw.rect(screen, GREEN, (self.x + 24, self.y - 48, 4, 4))
        pygame.draw.rect(screen, GREEN, (self.x + 44, self.y - 48, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 28, self.y - 48, 16, 8))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 24, self.y - 44, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 44, self.y - 44, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 20, self.y - 52, 32, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 20, self.y - 56, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 48, self.y - 56, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 24, self.y - 56, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 44, self.y - 56, 4, 4))
        pygame.draw.rect(screen, GREEN, (self.x + 28, self.y - 56, 16, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 24, self.y - 60, 4, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 44, self.y - 60, 4, 4))
        pygame.draw.rect(screen, DARK_GREEN, (self.x + 28, self.y - 60, 16, 4))
        pygame.draw.rect(screen, BLACK, (self.x + 28, self.y - 64, 16, 4))
        pygame.draw.rect(screen, BROWN, (0, 600 , 1200, 80))
        cannon_longueur = 40  # Longueur du canon
        cannon_start = (self.x + 9 * 4, self.y - 60)  # Point de départ du canon
        cannon_end_x = cannon_start[0] + cannon_longueur * math.cos(math.radians(angle))
        cannon_end_y = cannon_start[1] - cannon_longueur * math.sin(math.radians(angle))
        pygame.draw.line(screen, DARK_GREEN, cannon_start, (cannon_end_x, cannon_end_y), 5)  # Dessiner le canon
        return cannon_end_x, cannon_end_y  # Retourner la position de l'extrémité du canon
