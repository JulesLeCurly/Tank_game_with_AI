# Créé par Eleve, le 03/04/2025 en Python 3.7
# Version avec le canon qui peut tourner avec l'angle de tir et
# où la balle part depuis le bout du canon.

import pygame
import random
import math

class Balle:   # Classe pour représenter la balle
    def __init__(self, x, y, rayon, angle, vitesse, vitesse_tank):
        self.rayon = rayon
        self.x = x
        self.y = y
        self.gravité = 0.5
        self.angle_rad = math.radians(angle)
        self.Vitesse_x = vitesse * math.cos(self.angle_rad) + vitesse_tank
        self.Vitesse_y = -vitesse * math.sin(self.angle_rad)  # Négatif car l'axe Y est inversé
        self.visible = True

    def update(self):
        if self.visible:
            self.x += self.Vitesse_x
            self.y += self.Vitesse_y
            self.Vitesse_y += self.gravité
            if self.x < -self.rayon or self.x > width + self.rayon or self.y > 595 or self.y > height + self.rayon:  # Vérifier si la balle dépasse les bords de la fenêtre
                self.visible = False  # La balle disparaît
                return (self.x, self.y)  # Retourner la position de la balle avant de disparaître
        return None

    def draw(self, screen):
        if self.visible:
            pygame.draw.circle(screen, (120, 200, 0), (int(self.x), int(self.y)), self.rayon)

class Particule:  # Classe pour représenter une particule
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.lifetime = random.uniform(0, 150)  # Durée de vie de la particule
        self.gravité = 0.1  # Gravité initiale
        self.rayon = random.uniform(0, 4)

    def update(self):
        self.x += self.vx
        self.y += self.vy + self.gravité  # Appliquer la gravité
        self.gravité += 0.03  # Augmenter la gravité à chaque mise à jour
        self.lifetime -= 1
        self.rayon -= 0.015

    def draw(self, screen):
        if self.lifetime > 0:
            pygame.draw.circle(screen, (150, 255, 0), (int(self.x), int(self.y)), int(self.rayon))


class Cible:   # Classe pour représenter la cible
    def __init__(self):
        self.width = 40
        self.height = 40
        self.x = random.randint(0, width - self.width)
        self.y = random.randint(0, 540 - self.height)

    def reset_position(self):
        self.x = random.randint(0, width - self.width)
        self.y = random.randint(0, 540 - self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (255, 255, 255), (self.x + 5, self.y + 5, self.width - 10, self.height - 10))
        pygame.draw.rect(screen, (255, 0, 0), (self.x + 10, self.y + 10, self.width - 20, self.height - 20))
        pygame.draw.rect(screen, (255, 255, 255), (self.x + 17, self.y + 17, self.width - 34, self.height - 34))


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


pygame.init()  # Initialiser Pygame
width, height = 1200, 650
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Créer une instance de Balle, Cible et Tank
initial_vitesse = 10
max_vitesse = 35
initial_angle = 45
balle = None  # Initialiser la balle à None
cible = Cible()
tank = Tank(20, 600)  # Position initiale du tank

balles = []      # Liste pour stocker les balles
particules = []  # Liste pour stocker les particules
score = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()  # Gérer les entrées
    tank.update(keys)  # Mettre à jour la position du tank

    if keys[pygame.K_LEFT]:  # Augmenter l'angle
        initial_angle = min(180, initial_angle + 0.4)  # Ne pas dépasser 180
    if keys[pygame.K_RIGHT]:  # Diminuer l'angle
        initial_angle = max(0, initial_angle - 0.4)
    if keys[pygame.K_DOWN]:  # Diminuer la vitesse
        initial_vitesse = max(1, initial_vitesse - 0.1)  # Ne pas descendre en dessous de 1
    if keys[pygame.K_UP]:  # Augmenter la vitesse
        initial_vitesse += 0.1
        if initial_vitesse > max_vitesse:
            initial_vitesse = max_vitesse
    if keys[pygame.K_SPACE]:  # Tirer la balle avec la touche espace
        if balle is None or not balle.visible:  # Si aucune balle n'est active
            cannon_end_x, cannon_end_y = tank.draw(screen, initial_angle)  # Obtenir la position de l'extrémité du canon
            balle = Balle(cannon_end_x, cannon_end_y, 5, initial_angle, initial_vitesse, tank.vitesse * tank.direction)  # Créer la balle à la position du canon

    if balle is not None:  # Mettre à jour la balle et vérifier si elle disparaît
        position_disparition = balle.update()
        if position_disparition:
            for _ in range(100):  # Créer des particules à la position de la balle
                particules.append(Particule(position_disparition[0], position_disparition[1]))

    if balle is not None and balle.visible:  # Vérifier la collision avec la cible
        balle_rect = pygame.Rect(balle.x - balle.rayon, balle.y - balle.rayon, balle.rayon * 2, balle.rayon * 2)
        cible_rect = pygame.Rect(cible.x, cible.y, cible.width, cible.height)
        if balle_rect.colliderect(cible_rect):
            score += 1
            cible.reset_position()  # Réinitialiser la position de la cible

    screen.fill((0, 0, 0))  # Effacer l'écran
    tank.draw(screen, initial_angle)  # Dessiner le tank

    if balle is not None:  # Dessiner la balle et la cible
        balle.draw(screen)
    cible.draw(screen)

    for particule in particules:  # Mettre à jour et dessiner les particules
        particule.update()
        particule.draw(screen)

    particules = [p for p in particules if p.lifetime > 0]  # Supprimer les particules qui ont expiré
    font = pygame.font.Font(None, 36)  # Afficher les paramètres actuels
    vitesse_text = font.render(f"Vitesse: {round(initial_vitesse)}", True, (255, 255, 255))
    angle_text = font.render(f"Angle: {round(initial_angle)}°", True, (255, 255, 255))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))                          # Afficher le score

    screen.blit(vitesse_text, (10, 10))  # Afficher la vitesse en haut à gauche
    screen.blit(angle_text, (10, 50))    # Afficher l'angle en dessous de la vitesse
    screen.blit(score_text, (10, 90))    # Afficher le score en dessous de l'angle

    pygame.display.flip()                # Mettre à jour l'affichage
    clock.tick(60)                       # Limiter la boucle à 60 FPS

pygame.quit()  # Quitter Pygame
