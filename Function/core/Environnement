import pygame

class Environnement:
    def __init__(self, sol_y=600, sol_width=1200, sol_height=80, sol_color=(139, 69, 19)):
        self.sol_y = sol_y
        self.sol_width = sol_width
        self.sol_height = sol_height
        self.sol_color = sol_color

    def draw_ground(self, screen):
        pygame.draw.rect(screen, self.sol_color, (0, self.sol_y, self.sol_width, self.sol_height))
