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
initial_vitesse = 10
max_vitesse = 35
initial_angle = 45
balle = None  # Initialiser la balle à None
cible = Cible.Cible(width, height)
tank = Tank.Tank(20, 600)  # Position initiale du tank
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
    tank.update(keys)  # Mettre à jour la position du tank

    if keys[pygame.K_LEFT]:  # Augmenter l'angle
        initial_angle = min(180, initial_angle + 0.8)  # Ne pas dépasser 180
    if keys[pygame.K_RIGHT]:  # Diminuer l'angle
        initial_angle = max(0, initial_angle - 0.8)
    if keys[pygame.K_DOWN]:  # Diminuer la vitesse
        initial_vitesse = max(1, initial_vitesse - 0.3)  # Ne pas descendre en dessous de 1
    if keys[pygame.K_UP]:  # Augmenter la vitesse
        initial_vitesse += 0.3
        if initial_vitesse > max_vitesse:
            initial_vitesse = max_vitesse
    if keys[pygame.K_SPACE]:  # Tirer la balle avec la touche espace
        if balle is None or not balle.visible:  # Si aucune balle n'est active
            cannon_end_x, cannon_end_y = tank.draw(screen, initial_angle)  # Obtenir la position de l'extrémité du canon
            balle = Balle.Balle(
                width,
                height,
                cannon_end_x,
                cannon_end_y, 5,
                initial_angle,
                initial_vitesse,
                tank.vitesse * tank.direction
            )  # Créer la balle à la position du canon

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
    tank.draw(screen, initial_angle)  # Dessiner le tank

    if balle is not None:  # Dessiner la balle et la cible
        balle.draw(screen)
    if afficher_cible:
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