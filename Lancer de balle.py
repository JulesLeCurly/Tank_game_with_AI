import pygame
import math

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lancer de Balle")

# Couleurs
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Paramètres de la balle
ball_radius = 2
ball_x = 100
ball_y = height - ball_radius
velocity = 0
gravity = 0.5
angle = 45  # Angle de lancement en degrés
speed = 10  # Vitesse initiale

# Convertir l'angle en radians
angle_rad = math.radians(angle)

# Calculer les composantes de la vitesse
velocity_x = speed * math.cos(angle_rad)
velocity_y = -speed * math.sin(angle_rad)  # Négatif car l'axe Y est inversé

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mettre à jour la position de la balle
    ball_x += velocity_x
    ball_y += velocity_y

    # Appliquer la gravité
    velocity_y += gravity

    # Vérifier si la balle touche le sol
    if ball_y >= height - ball_radius:
        ball_y = height - ball_radius
        velocity_y = 0  # Réinitialiser la vitesse verticale

    # Effacer l'écran
    screen.fill(WHITE)

    # Dessiner la balle
    pygame.draw.circle(screen, BLUE, (int(ball_x), int(ball_y)), ball_radius)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter la vitesse de la boucle
    pygame.time.delay(30)

# Quitter Pygame
pygame.quit()