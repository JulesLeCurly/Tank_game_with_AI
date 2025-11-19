import pygame

import Function.core.Balle as Balle
import Function.core.Tank as Tank
import Function.core.Cible as Cible
import Function.core.Particule as Particule
from Function.core.Terrain import Environnement


pygame.init()  # Initialiser Pygame
width, height = 1200, 650
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
env = Environnement()


color_tank_list = ["red", "blue", "green", "yellow"]

nb_tank = 2
Tanks_class = {}
for i in range(nb_tank):
    x_tank_spawn = (i + 1) * (width / (nb_tank +1))
    x_tank_spawn-=42.5
    Tanks_class[color_tank_list[i]] = Tank.Tank(
        width,
        height,
        x_tank_spawn,
        color_tank_list[i]
    )

# Créer une instance de Balle, Cible et Tank
max_puissance = 35
max_vitesse2 = 35
balle = None  # Initialiser la balle à None
cible = Cible.Cible(width, height)
afficher_cible=False


balles = []      # Liste pour stocker les balles
particules = []  # Liste pour stocker les particules
score = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()  # Gérer les entrées

    # Modifier l'angle
    if keys[pygame.K_a]:  # Augmenter l'angle
        Tanks_class["red"].angle = min(180, Tanks_class["red"].angle + 0.8)
    if keys[pygame.K_e]:  # Diminuer l'angle
        Tanks_class["red"].angle = max(0, Tanks_class["red"].angle - 0.8)

    # Modifier la vitesse (puissance)
    if keys[pygame.K_s]:  # Diminuer la puissance
        Tanks_class["red"].puissance = max(1, Tanks_class["red"].puissance - 0.3)
    if keys[pygame.K_z]:  # Augmenter la puissance
        Tanks_class["red"].puissance = min(max_vitesse2, Tanks_class["red"].puissance + 0.3)

    # Déplacement du tank
    if keys[pygame.K_q]:  # Aller à gauche (AZERTY)
        Tanks_class["red"].x -= Tanks_class["red"].vitesse
    if keys[pygame.K_d]:  # Aller à droite (AZERTY)
        Tanks_class["red"].x += Tanks_class["red"].vitesse

    # Tir
    if keys[pygame.K_f]:  # Tir avec Entrée
        cannon_end_x, cannon_end_y = Tanks_class["red"].draw(screen, Tanks_class["red"].angle)
        balles.append(Balle.Balle(
            width,
            height,
            cannon_end_x,
            cannon_end_y,
            5,
            Tanks_class["red"].angle,
            Tanks_class["red"].puissance,
            Tanks_class["red"].vitesse * Tanks_class["red"].direction,
            owner=Tanks_class["red"]
        ))




    # Modifier l'angle
    if keys[pygame.K_i]:  # Augmenter l'angle
        Tanks_class["blue"].angle = min(180, Tanks_class["blue"].angle + 0.8)
    if keys[pygame.K_p]:  # Diminuer l'angle
        Tanks_class["blue"].angle = max(0, Tanks_class["blue"].angle - 0.8)

    # Modifier la vitesse (puissance)
    if keys[pygame.K_l]:  # Diminuer la puissance
        Tanks_class["blue"].puissance = max(1, Tanks_class["blue"].puissance - 0.3)
    if keys[pygame.K_o]:  # Augmenter la puissance
        Tanks_class["blue"].puissance = min(max_vitesse2, Tanks_class["blue"].puissance + 0.3)

    # Déplacement du tank
    if keys[pygame.K_k]:  # Aller à gauche (AZERTY)
        Tanks_class["blue"].x -= Tanks_class["blue"].vitesse
    if keys[pygame.K_m]:  # Aller à droite (AZERTY)
        Tanks_class["blue"].x += Tanks_class["blue"].vitesse

    # Tir
    if keys[pygame.K_j]:  # Tir avec Entrée
        cannon_end_x, cannon_end_y = Tanks_class["blue"].draw(screen, Tanks_class["blue"].angle)
        balles.append(Balle.Balle(
            width,
            height,
            cannon_end_x,
            cannon_end_y,
            5,
            Tanks_class["blue"].angle,
            Tanks_class["blue"].puissance,
            Tanks_class["blue"].vitesse * Tanks_class["blue"].direction,
            owner=Tanks_class["blue"]
        ))


    if balles != []:  # Mettre à jour la balle et vérifier si elle disparaît
        for balle in balles:
            position_disparition = balle.update()
            if position_disparition:
                for _ in range(100):  # Créer des particules à la position de la balle
                    particules.append(Particule.Particule(position_disparition[0], position_disparition[1]))


    for tank_name in Tanks_class:
        if Tanks_class[tank_name].x < 0:
            Tanks_class[tank_name].x =0
        if Tanks_class[tank_name].x > width-85:
            Tanks_class[tank_name].x = width-85

    if balle is not None and balle.visible and afficher_cible:  # Vérifier la collision avec la cible
        balle_rect = pygame.Rect(balle.x - balle.rayon, balle.y - balle.rayon, balle.rayon * 2, balle.rayon * 2)
        cible_rect = pygame.Rect(cible.x, cible.y, cible.width, cible.height)
        if balle_rect.colliderect(cible_rect):
            score += 1
            cible.reset_position()  # Réinitialiser la position de la cible

    screen.fill((0, 0, 0))  # Effacer l'écran
    env.draw_ground(screen)

    for balle in balles:
        for tank_name, tank in Tanks_class.items():

            # Empêcher qu’un tank touche son propre tireur
            if balle.owner == tank:
                continue


    for tank_name in Tanks_class:
        Tanks_class[tank_name].draw(screen, Tanks_class[tank_name].angle)
    
    if balles != []:  # Mettre à jour la balle et vérifier si elle disparaît
        for balle in balles:
            balle.draw(screen)
    if afficher_cible:
        cible.draw(screen)

    for balle in balles:
        for name, tank in Tanks_class.items():
            if tank.hit(balle):
                print(name, "touché !")
                balle.visible = False

    for particule in particules:  # Mettre à jour et dessiner les particules
        particule.update()
        particule.draw(screen)

    particules = [p for p in particules if p.lifetime > 0]  # Supprimer les particules qui ont expiré
    font = pygame.font.Font(None, 36)  # Afficher les paramètres actuels
    vitesse_text1 = font.render(f"Vitesse: {round(Tanks_class['red'].puissance)}", True, (255, 255, 255))
    angle_text1 = font.render(f"Angle: {round(Tanks_class['red'].angle)}°", True, (255, 255, 255))
    score_text1 = font.render(f"Score: {score}", True, (255, 255, 255))                          # Afficher le score
    vitesse_text2 = font.render(f"Vitesse: {round(Tanks_class['blue'].puissance)}", True, (255, 255, 255))
    angle_text2 = font.render(f"Angle: {round(Tanks_class['blue'].angle)}°", True, (255, 255, 255))
    score_text2 = font.render(f"Score: {score}", True, (255, 255, 255))                          # Afficher le score

    screen.blit(vitesse_text1, (10, 10))  # Afficher la vitesse en haut à gauche
    screen.blit(angle_text1, (10, 50))    # Afficher l'angle en dessous de la vitesse
    screen.blit(score_text1, (10, 90))    # Afficher le score en dessous de l'angle
    screen.blit(vitesse_text2, (1040, 10))  # Afficher la vitesse en haut à gauche
    screen.blit(angle_text2, (1040, 50))    # Afficher l'angle en dessous de la vitesse
    screen.blit(score_text2, (1040, 90))    # Afficher le score en dessous de l'angle


    pygame.display.flip()                # Mettre à jour l'affichage
    clock.tick(60)                       # Limiter la boucle à 60 FPS

pygame.quit()  # Quitter Pygame