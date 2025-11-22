import pygame
import random
import math
import numpy as np
from PIL import Image
import os

class Terrain:
    def __init__(self, width, height, sol_y=500, sol_width=1200, sol_height=80, sol_color=(139, 69, 19)):
        self.sol_y = sol_y
        self.sol_width = sol_width
        self.sol_height = sol_height
        self.sol_color = sol_color

        self.width = width
        self.height = height

        self.path = f"Images/Terrains/Terrain.png"


    def draw_ground(self, screen):
        screen.blit(self.image_Terrains, (0, 0))
    
    def generer_terrain_brute(self, nb_points=1200, amplitude=20.0, pente_max=2.0, frequence=0.01):
        x = list(range(nb_points))
        y = [0.0] * nb_points

        for i in range(1, nb_points):
            bruit = (random.random() - 0.5) * 2.0
            variation = bruit * pente_max
            sinus = math.sin(i * frequence) * amplitude

            y[i] = y[i-1] + variation + sinus * 0.01

        return x, y

    def lisser_courbe(self, y, window_size=8):
        n = len(y)
        result = [0.0] * n
        for i in range(n):
            debut = max(0, i - window_size)
            fin = min(n, i + window_size + 1)
            result[i] = sum(y[debut:fin]) / (fin - debut)
        return result
    
    def generate_image(self, y_brut, width, height):
        # Vérifications simples
        y_brut = np.asarray(y_brut, dtype=int)
        if len(y_brut) != width:
            raise ValueError("La longueur de y_brut doit être égale à width")
        if np.any(y_brut < 0) or np.any(y_brut >= height):
            print(np.any(y_brut < 0), y_brut.min())
            print(np.any(y_brut >= height), y_brut.max(), height)
            raise ValueError("Les valeurs de y_brut doivent être dans [0, height-1]")

        # Image RGBA (transparent par défaut)
        img = np.zeros((height, width, 4), dtype=np.uint8)

        # Couleur brune
        brown = np.array([110, 200, 20, 255], dtype=np.uint8)

        # Remplissage : pour chaque x, remplir du bas jusqu'à y
        for x in range(width):
            y = y_brut[x]
            img[y:height, x] = brown   # Du tracé vers le bas → brun
            # Le reste reste transparent

        return Image.fromarray(img, mode="RGBA")

    def generate_terrain(self,):
        y_brut = np.array([-1])
        lissage = 2

        while True:
            x, y_brut = self.generer_terrain_brute(nb_points=1200, amplitude=6.0, pente_max=10, frequence=0.1)
            for i in range(lissage):
                y_brut = self.lisser_courbe(y_brut, window_size=100)

            y_affiche = np.array(y_brut) + self.sol_y

            if y_affiche.min() >= 0 and y_affiche.max() < self.height:
                break

        self.array_terrain = np.array(y_brut) + self.sol_y  # sans décalage
        terrain_pixels = self.array_terrain
        Terrain_image = self.generate_image(terrain_pixels, width=self.width, height=self.height)

        os.makedirs("Images/Terrains", exist_ok=True)
        Terrain_image.save("Images/Terrains/Terrain.png")

        
        self.image_Terrains = pygame.image.load(self.path)