# Créé par bmeyer52, le 11/03/2025 en Python 3.7
# Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *

# Initialisation de la bibliothèque Pygame
pygame.init()

# Création de la fenêtre
fenetre = pygame.display.set_mode((1000, 800))

# Variable qui continue la boucle si = 1, stoppe si = 0
continuer = True

# Chargement et collage du fond
fond = pygame.image.load("fonds.png")
fenetre.blit(fond, (0, 0))

# Chargement et collage du personnage
perso = pygame.image.load("char.png").convert()

# Redimensionnement du personnage
largeur_nouvelle = 75  # Nouvelle largeur
hauteur_nouvelle = 90   # Nouvelle hauteur
perso_redimensionne = pygame.transform.scale(perso, (largeur_nouvelle, hauteur_nouvelle))

# Collage du personnage redimensionné
fenetre.blit(perso_redimensionne, (300, 300))

# Rafraîchissement de l'écran
pygame.display.flip()

# Boucle infinie
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:  # Vérifie si l'événement est la fermeture de la fenêtre
            continuer = False

    # Ici, vous pouvez ajouter d'autres instructions pour mettre à jour le jeu

# Quitter Pygame
pygame.quit()