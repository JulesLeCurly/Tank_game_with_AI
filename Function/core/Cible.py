import random
import pygame

class Cible:   # Classe pour représenter la cible
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width = 40
        self.height = 40
        self.x = random.randint(0, self.screen_width - self.width)
        self.y = random.randint(0, 540 - self.height)

    def reset_position(self):
        self.x = random.randint(0, self.screen_width - self.width)
        self.y = random.randint(0, 540 - self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (255, 255, 255), (self.x + 5, self.y + 5, self.width - 10, self.height - 10))
        pygame.draw.rect(screen, (255, 0, 0), (self.x + 10, self.y + 10, self.width - 20, self.height - 20))
        pygame.draw.rect(screen, (255, 255, 255), (self.x + 17, self.y + 17, self.width - 34, self.height - 34))
