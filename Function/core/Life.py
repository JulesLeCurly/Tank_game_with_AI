import pygame

class Life:
    def __init__(self, color, scale=2):
        """
        color = 'red' ou 'blue'
        scale = facteur de taille (2 = x2, 3 = x3, etc.)
        """
        self.color = color
        self.scale = scale

        # ----- Chargement des sprites -----
        img_red  = pygame.image.load("Images/lifeheart_red.png").convert_alpha()
        img_blue = pygame.image.load("Images/lifeheart_blue.png").convert_alpha()
        img_gray = pygame.image.load("Images/lifeheart_gray.png").convert_alpha()

        # ----- Resize -----
        w = img_red.get_width()  * scale
        h = img_red.get_height() * scale

        self.img_red  = pygame.transform.scale(img_red,  (w, h))
        self.img_blue = pygame.transform.scale(img_blue, (w, h))
        self.img_empty = pygame.transform.scale(img_gray, (w, h))

        self.spacing = 10 * scale
        self.heart_w = self.img_red.get_width()

    def draw(self, screen, hp, hp_max, x, y):
        """
        Affiche les points de vie du tank
        """
        for i in range(hp_max):
            xpos = x + i * (self.heart_w + self.spacing)

            if i < hp:
                if self.color == "red":
                    screen.blit(self.img_red, (xpos, y))
                else:
                    screen.blit(self.img_blue, (xpos, y))
            else:
                screen.blit(self.img_empty, (xpos, y))
