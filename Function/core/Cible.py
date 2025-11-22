import random
import pygame


class Cible:
    """Cible rectangulaire avec position aléatoire."""

    def __init__(self, screen_width, screen_height):

        self.screen_width = screen_width
        self.screen_height = screen_height

        # Taille de la cible
        self.width = 40
        self.height = 40

        # Position initiale
        self.x = random.randint(0, self.screen_width - self.width)
        self.y = random.randint(0, 540 - self.height)


    # ================================================================
    # 🔵 Réinitialisation de la position
    # ================================================================
    def reset_position(self):
        self.x = random.randint(0, self.screen_width - self.width)
        self.y = random.randint(0, 540 - self.height)


    # ================================================================
    # 🔵 Affichage (cible avec 4 carrés concentriques)
    # ================================================================
    def draw(self, screen):
        # Carré extérieur (rouge)
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.x, self.y, self.width, self.height))

        # Carré blanc
        pygame.draw.rect(screen, (255, 255, 255),
                         (self.x + 5, self.y + 5, self.width - 10, self.height - 10))

        # Carré rouge intérieur
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.x + 10, self.y + 10, self.width - 20, self.height - 20))

        # Petit carré blanc au centre
        pygame.draw.rect(screen, (255, 255, 255),
                         (self.x + 17, self.y + 17, self.width - 34, self.height - 34))
