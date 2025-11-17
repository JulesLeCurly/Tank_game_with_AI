# Jeu Canon - PyClub
# Créé par Jérôme REDLER, le 11/03/2025 en Python 3.7
#
import pygame
import random

# ----------------- Définition des classes d'objet -----------------------------
class Particule:    # particules de l'explosion
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.lifetime = 100  # Durée de vie de la particule

    def Maj(self):
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 1

    def Dessiner(self, screen):
        if self.lifetime > 0:
            pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), 2)

class Canon:        # gestion du canon
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Maj(self):
        a=1

    def Dessiner(self, screen):
        a=1

class Bombe:        # gestion de la bombe
    def __init__(self, x, y, vitesse, angle):
        self.x = x
        self.y = y
        self.vitesse = vitesse
        self.angle = angle

    def Maj(self):
        a=1

    def Dessiner(self, screen):
        a=1

class Joueur:
    def __init__(self, x, y, vitesse):
        self.x = x
        self.y = y

    def Maj(self):
        a=1

    def Dessiner(self, screen):
        a=1


# ------------------ Initialiser Pygame et Objets ------------------------------
pygame.init()
screen = pygame.display.set_mode((1200, 800))   # taille du jeu 1200x800
clock = pygame.time.Clock()
width, height = 1200, 800

# ------------------ Déclaration des fonctions ---------------------------------




# ------------------ Initialisation des affichages -----------------------------

class TextJoueur1:
    def draw_text1(self, surface, text, position, font_size=36, color=(255, 255, 255)):
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, position)


class TextAngle1:
    def draw_textangle1(self, surface, text, position, font_size=26, color=(255, 255, 255)):
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, position)

class TextVitesse1:
    def draw_textvitesse1(self, surface, text, position, font_size=26, color=(255, 255, 255)):
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, position)


class Compteur1:
    def __init__(self, width, height):
        self.compteur = 0
        self.width = width
        self.height = height
        self.rect = pygame.Rect(20, 100, 120, 55)  # Rectangle pour le texte
        self.font = pygame.font.Font(None, 74)


    def draw_text(self):
        text_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        text_surface.fill((255, 255, 255, 0))  # Remplir la surface avec transparence


        # Dessiner le rectangle
        pygame.draw.rect(text_surface, (255, 255, 255), (0, 0, self.rect.width, self.rect.height))  # Couleur gris clair
        text = self.font.render(str(self.compteur), True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.rect.width // 2, self.rect.height // 2))  # Centrer le texte
        text_surface.blit(text, text_rect)


        return text_surface


    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:  # Incrémenter le compteur
                if self.compteur < 90:
                    self.compteur += 1
            elif event.key == pygame.K_a:  # Décrémenter le compteur
                if self.compteur > 0:
                    self.compteur -= 1

class Compteur2:
    def __init__(self, width, height):
        self.compteur = 0
        self.width = width
        self.height = height
        self.rect = pygame.Rect(20, 200, 120, 55)  # Rectangle pour le texte
        self.font = pygame.font.Font(None, 74)


    def draw_text(self):
        text_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        text_surface.fill((255, 255, 255, 0))  # Remplir la surface avec transparence


        # Dessiner le rectangle
        pygame.draw.rect(text_surface, (255, 255, 255), (0, 0, self.rect.width, self.rect.height))
        text = self.font.render(str(self.compteur), True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.rect.width // 2, self.rect.height // 2))  # Centrer le texte
        text_surface.blit(text, text_rect)


        return text_surface


    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  # Incrémenter le compteur
                if self.compteur < 90:
                    self.compteur += 1
            elif event.key == pygame.K_q:  # Décrémenter le compteur
                if self.compteur > 0:
                    self.compteur -= 1


# Création des objets de texte

drawer1 = TextJoueur1()

drawer2 = TextAngle1()

drawer3 = TextVitesse1()

compteur_1 = Compteur1(width, height)

compteur_2 = Compteur2(width, height)




# ------------------ Boucle du Jeu ---------------------------------------------

# Boucle principale

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        compteur_1.update(event)  # Mettre à jour le compteur1 en fonction des événements
        compteur_2.update(event)  # Mettre à jour le compteur2 en fonction des événements

    drawer1.draw_text1(screen, "Joueur 1 :", (20, 50))
    drawer2.draw_textangle1(screen, "Angle :", (25, 78))
    drawer3.draw_textvitesse1(screen, "Vitesse :", (40, 100))


    # Dessiner le compteur1
    text_surface = compteur_1.draw_text()
    screen.blit(text_surface, (compteur_1.rect.x, compteur_1.rect.y))

    # Dessiner le compteur2
    text_surface = compteur_2.draw_text()
    screen.blit(text_surface, (compteur_2.rect.x, compteur_2.rect.y))


    pygame.display.flip()

    clock.tick(60)

pygame.quit()