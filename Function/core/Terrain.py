import pygame
import random
import math
import numpy as np
from PIL import Image
import os


class Terrain:
    def __init__(self, width, height, terrain_interval=[15, 60], sol_color=(139, 69, 19)):

        # Données du sol
        self.sol_color = sol_color

        # Dimensions écran
        self.width = width
        self.height = height

        self.terrain_interval = terrain_interval

        # Chemin image terrain
        self.path = "Images/Terrains/Terrain.png"


    # ====================================================
    # 🔵 DESSIN DU TERRAIN
    # ====================================================
    def draw_ground(self, screen):
        screen.blit(self.image_Terrains, (0, 0))


    # ====================================================
    # 🔵 GÉNÉRATION COURBE BRUTE
    # ====================================================
    def generer_terrain_brute(self, nb_points=1200, amplitude=20.0, pente_max=2.0, frequence=0.01):

        x = list(range(nb_points))
        y = [0.0] * nb_points

        for i in range(1, nb_points):

            bruit = (random.random() - 0.5) * 2.0
            variation = bruit * pente_max

            sinus = math.sin(i * frequence) * amplitude

            y[i] = y[i-1] + variation + sinus * 0.01

        return x, y


    # ====================================================
    # 🔵 LISSEUR DE COURBE
    # ====================================================
    def lisser_courbe(self, y, window_size=8):

        n = len(y)
        result = [0.0] * n

        for i in range(n):
            debut = max(0, i - window_size)
            fin   = min(n, i + window_size + 1)

            result[i] = sum(y[debut:fin]) / (fin - debut)

        return result


    # ====================================================
    # 🔵 CRÉATION D'UNE IMAGE RGBA DU TERRAIN
    # ====================================================
    def generate_image(self, y_brut, width, height):

        # Vérification
        y_brut = np.asarray(y_brut, dtype=int)

        if len(y_brut) != width:
            raise ValueError("La longueur de y_brut doit être égale à width")

        if np.any(y_brut < 0) or np.any(y_brut >= height):
            raise ValueError("Les valeurs de y_brut doivent être dans [0, height-1]")

        # Image vide transparente
        img = np.zeros((height, width, 4), dtype=np.uint8)

        green = np.array([110, 200, 20, 255], dtype=np.uint8)
        brown = np.array([139, 69, 19, 255], dtype=np.uint8)

        # Remplir colonne par colonne
        for x in range(width):

            y = y_brut[x]

            img[y:y+10, x]     = green   # herbe
            img[y+10:height, x] = brown  # terre

        return Image.fromarray(img, mode="RGBA")


    # ====================================================
    # 🔵 GÉNÉRATION COMPLÈTE DU TERRAIN + EXPORT IMAGE
    # ====================================================
    def generate_terrain(self):

        y_brut = np.array([-1])  # pour entrer dans la boucle

        x, y_brut = self.generer_terrain_brute(
            nb_points=self.width,
            amplitude=1.5,
            pente_max=1,
            frequence=6
        )

        nb_lissage = 4
        for _ in range(nb_lissage):
            y_brut = self.lisser_courbe(y_brut, window_size=100)

        # Stockage
        self.array_terrain = np.array(y_brut)

        # Nouveau range
        new_min = self.height * (self.terrain_interval[0] / 100)
        new_max = self.height * (self.terrain_interval[1] / 100)

        # Min et max actuels
        xmin = self.array_terrain.min()
        xmax = self.array_terrain.max()

        # Scaling
        self.array_terrain = ((self.array_terrain - xmin) / (xmax - xmin)) * (new_max - new_min) + new_min

        # Conversion
        self.array_terrain = self.height - self.array_terrain

        # Création de l'image
        terrain_img = self.generate_image(
            self.array_terrain,
            width=self.width,
            height=self.height
        )

        # Sauvegarde
        os.makedirs("Images/Terrains", exist_ok=True)
        terrain_img.save(self.path)

        # Chargement pygame
        self.image_Terrains = pygame.image.load(self.path)
    
    def change_terrain_at(self, x_center, y_center, radius=8):
        x_center = int(x_center)
        y_center = int(y_center)

        for x in range(x_center - radius, x_center + radius + 1):
            self.array_terrain[x] = max(self.array_terrain[x], y_center + math.sqrt(radius**2 - (x - x_center)**2))

        # Re-generate terrain image after modification
        terrain_img = self.generate_image(
            self.array_terrain,
            width=self.width,
            height=self.height
        )
        terrain_img.save(self.path)
        self.image_Terrains = pygame.image.load(self.path)

        print(f"Terrain modified at ({x_center}, {y_center}) with radius {radius}")
