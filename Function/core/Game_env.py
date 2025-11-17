import pygame

import Function.core.Balle as Balle
import Function.core.Tank as Tank
import Function.core.Cible as Cible
import Function.core.Particule as Particule



pygame.init()  # Initialiser Pygame
width, height = 1200, 650
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Créer une instance de Balle, Cible et Tank
initial_vitesse1 = 10
max_vitesse1 = 35
initial_angle1 = 45
initial_vitesse2 = 10
max_vitesse2 = 35
initial_angle2 = 125
balle = None  # Initialiser la balle à None
cible = Cible.Cible(width, height)
tank1 = Tank.Tank(20, 600)  # Position initiale du tank1
tank2 = Tank.Tank(1080, 600)  # Position initiale du tank2
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

    if keys[pygame.K_LEFT]:  # Augmenter l'angle
        initial_angle1 = min(180, initial_angle1 + 0.8)  # Ne pas dépasser 180
    if keys[pygame.K_RIGHT]:  # Diminuer l'angle
        initial_angle1 = max(0, initial_angle1 - 0.8)
    if keys[pygame.K_DOWN]:  # Diminuer la vitesse
        initial_vitesse1 = max(1, initial_vitesse1 - 0.3)  # Ne pas descendre en dessous de 1
    if keys[pygame.K_UP]:  # Augmenter la vitesse
        initial_vitesse1 += 0.3
        if initial_vitesse1 > max_vitesse1:
            initial_vitesse1 = max_vitesse1
    # Déplacement du tank
    if keys[pygame.K_q]:  # Aller à gauche (AZERTY)
        tank1.x -= tank1.vitesse
    if keys[pygame.K_d]:  # Aller à droite (AZERTY)
        tank1.x += tank1.vitesse
    if keys[pygame.K_SPACE]:  # Tirer la balle avec la touche espace
        if balle is None or not balle.visible:  # Si aucune balle n'est active
            cannon_end_x, cannon_end_y = tank1.draw(screen, initial_angle1)  # Obtenir la position de l'extrémité du canon
            balle = Balle.Balle(
                width,
                height,
                cannon_end_x,
                cannon_end_y, 5,
                initial_angle1,
                initial_vitesse1,
                tank1.vitesse * tank1.direction
            )  # Créer la balle à la position du canon



    # Modifier l'angle
    if keys[pygame.K_KP1]:  # Augmenter l'angle
        initial_angle2 = min(180, initial_angle2 + 0.8)
    if keys[pygame.K_KP3]:  # Diminuer l'angle
        initial_angle2 = max(0, initial_angle2 - 0.8)

    # Modifier la vitesse (puissance)
    if keys[pygame.K_KP5]:  # Diminuer la puissance
        initial_vitesse2 = max(1, initial_vitesse2 - 0.3)
    if keys[pygame.K_KP2]:  # Augmenter la puissance
        initial_vitesse2 = min(max_vitesse2, initial_vitesse2 + 0.3)

    # Déplacement du tank
    if keys[pygame.K_k]:  # Aller à gauche (AZERTY)
        tank2.x -= tank2.vitesse
    if keys[pygame.K_m]:  # Aller à droite (AZERTY)
        tank2.x += tank2.vitesse

    # Tir
    if keys[pygame.K_RETURN]:  # Tir avec Entrée
        if balle is None or not balle.visible:
            cannon_end_x, cannon_end_y = tank2.draw(screen, initial_angle2)
            balle = Balle.Balle(
                width,
                height,
                cannon_end_x,
                cannon_end_y,
                5,
                initial_angle2,
                initial_vitesse2,
                tank2.vitesse * tank2.direction
            )


    if balle is not None:  # Mettre à jour la balle et vérifier si elle disparaît
        position_disparition = balle.update()
        if position_disparition:
            for _ in range(100):  # Créer des particules à la position de la balle
                particules.append(Particule.Particule(position_disparition[0], position_disparition[1]))



    if balle is not None and balle.visible and afficher_cible:  # Vérifier la collision avec la cible
        balle_rect = pygame.Rect(balle.x - balle.rayon, balle.y - balle.rayon, balle.rayon * 2, balle.rayon * 2)
        cible_rect = pygame.Rect(cible.x, cible.y, cible.width, cible.height)
        if balle_rect.colliderect(cible_rect):
            score += 1
            cible.reset_position()  # Réinitialiser la position de la cible

    screen.fill((0, 0, 0))  # Effacer l'écran
    tank1.draw(screen, initial_angle1)  # Dessiner le tank1
    tank2.draw(screen, initial_angle2)  # Dessiner le tank2

    if balle is not None:  # Dessiner la balle et la cible
        balle.draw(screen)
    if afficher_cible:
        cible.draw(screen)

    for particule in particules:  # Mettre à jour et dessiner les particules
        particule.update()
        particule.draw(screen)

    particules = [p for p in particules if p.lifetime > 0]  # Supprimer les particules qui ont expiré
    font = pygame.font.Font(None, 36)  # Afficher les paramètres actuels
    vitesse_text = font.render(f"Vitesse: {round(initial_vitesse1)}", True, (255, 255, 255))
    angle_text = font.render(f"Angle: {round(initial_angle1)}°", True, (255, 255, 255))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))                          # Afficher le score

    screen.blit(vitesse_text, (10, 10))  # Afficher la vitesse en haut à gauche
    screen.blit(angle_text, (10, 50))    # Afficher l'angle en dessous de la vitesse
    screen.blit(score_text, (10, 90))    # Afficher le score en dessous de l'angle

    pygame.display.flip()                # Mettre à jour l'affichage
    clock.tick(60)                       # Limiter la boucle à 60 FPS

pygame.quit()  # Quitter Pygame