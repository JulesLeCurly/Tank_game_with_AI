import pygame
from colorama import Fore, Style, init

import Function.core.Balle as Balle
import Function.core.Tank as Tank
import Function.core.Cible as Cible
import Function.core.Particule as Particule
from Function.core.Terrain import Terrain


pygame.init()  # Initialiser Pygame

width, height = 1200, 650
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

Terrain_class = Terrain(width, height)
Terrain_class.generate_terrain()

color_tank_list = ["red", "blue", "green", "yellow"]

nb_tank = 2

Tanks_class = {}

# --- Création des tanks ---
for i in range(nb_tank):
    x_tank_spawn = (i + 1) * (width / (nb_tank + 1))
    x_tank_spawn -= 42.5
    Tanks_class[color_tank_list[i]] = Tank.Tank(
        width,
        height,
        x_tank_spawn,
        color_tank_list[i]
    )

# --- Instances de base ---
max_puissance = 35
max_vitesse2 = 35
balle = None
cible = Cible.Cible(width, height)
afficher_cible = False

balles = []
particules = []
score = 0

running = True


# ---------------------------------------------------------------------------
#                               BOUCLE DU JEU
# ---------------------------------------------------------------------------
while running:
    # --------------------- ÉVÉNEMENTS ---------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # ------------------ CONTROLES TANK ROUGE ------------------
    if keys[pygame.K_a]:
        Tanks_class["red"].angle = min(180, Tanks_class["red"].angle + 0.8)
    if keys[pygame.K_e]:
        Tanks_class["red"].angle = max(0, Tanks_class["red"].angle - 0.8)

    if keys[pygame.K_s]:
        Tanks_class["red"].puissance = max(5, Tanks_class["red"].puissance - 0.3)
    if keys[pygame.K_z]:
        Tanks_class["red"].puissance = min(max_vitesse2, Tanks_class["red"].puissance + 0.3)

    if keys[pygame.K_q]:
        Tanks_class["red"].x -= Tanks_class["red"].vitesse
    if keys[pygame.K_d]:
        Tanks_class["red"].x += Tanks_class["red"].vitesse

    if keys[pygame.K_f] and Tanks_class["red"].can_shoot:
        cannon_end_x, cannon_end_y = Tanks_class["red"].draw(screen, Terrain_class.array_terrain)
        balles.append(Balle.Balle(
            width, height, cannon_end_x, cannon_end_y,
            5, Tanks_class["red"].angle, Tanks_class["red"].puissance,
            Tanks_class["red"].vitesse * Tanks_class["red"].direction,
            owner=Tanks_class["red"], color_tank ="red"
            ))
        Tanks_class["red"].can_shoot = False

    # ------------------ CONTROLES TANK BLEU ------------------
    if keys[pygame.K_i]:
        Tanks_class["blue"].angle = min(180, Tanks_class["blue"].angle + 0.8)
    if keys[pygame.K_p]:
        Tanks_class["blue"].angle = max(0, Tanks_class["blue"].angle - 0.8)

    if keys[pygame.K_l]:
        Tanks_class["blue"].puissance = max(5, Tanks_class["blue"].puissance - 0.3)
    if keys[pygame.K_o]:
        Tanks_class["blue"].puissance = min(max_vitesse2, Tanks_class["blue"].puissance + 0.3)

    if keys[pygame.K_k]:
        Tanks_class["blue"].x -= Tanks_class["blue"].vitesse
    if keys[pygame.K_m]:
        Tanks_class["blue"].x += Tanks_class["blue"].vitesse

    if keys[pygame.K_j] and Tanks_class["blue"].can_shoot:
        cannon_end_x, cannon_end_y = Tanks_class["blue"].draw(screen, Terrain_class.array_terrain)
        balles.append(Balle.Balle(
            width, height, cannon_end_x, cannon_end_y,
            5, Tanks_class["blue"].angle, Tanks_class["blue"].puissance,
            Tanks_class["blue"].vitesse * Tanks_class["blue"].direction,
            owner=Tanks_class["blue"], color_tank = "blue"
        ))
        Tanks_class["blue"].can_shoot = False

    # --------------------- UPDATE BALLES ---------------------
    for balle in list(balles):
        position_disparition = balle.update()

        if position_disparition:
            balle.owner.can_shoot = True

            # particules explosion
            for _ in range(100):
                particules.append(
                    Particule.Particule(position_disparition[0], position_disparition[1], balle.color)
                )

    # --------------------- LIMITE DU TERRAIN ---------------------
    for tank_name in Tanks_class:
        if Tanks_class[tank_name].x < 0:
            Tanks_class[tank_name].x = 0
        if Tanks_class[tank_name].x > width - 85:
            Tanks_class[tank_name].x = width - 85

    # --------------------- DESSIN ÉCRAN ---------------------
    screen.fill((0,110,220))
    Terrain_class.draw_ground(screen)

    # --------------------- DESSIN TANKS ---------------------
    for tank_name in Tanks_class:
        Tanks_class[tank_name].draw(screen, Terrain_class.array_terrain)

    # --------------------- DESSIN BALLES ---------------------
    for balle in list(balles):
        if balle.visible:
            balle.draw(screen)
        else:
            balles.remove(balle)
            continue

        # ------------------ COLLISION BALLE / TANK ------------------
        for name, tank in Tanks_class.items():

            if tank == balle.owner:
                continue

            if tank.hit(balle):

                print(getattr(Fore, name.upper()) + f"{name} touché !" + Style.RESET_ALL)

                tank.hp -= 1

                if tank.hp <= 0:
                    print(getattr(Fore, name.upper()) + f"{name} LOSE !" + Style.RESET_ALL)

                balle.owner.can_shoot = True

                balle.visible = False
                balles.remove(balle)
                break

    # --------------------- PARTICULES ---------------------
    for particule in particules:
        particule.update()
        particule.draw(screen)

    particules = [p for p in particules if p.lifetime > 0]

    # --------------------- UI ---------------------
    font = pygame.font.Font(None, 36)

    # ROUGE
    screen.blit(font.render(f"Vitesse: {round(Tanks_class['red'].puissance)}", True, (255, 255, 255)), (10, 10))
    screen.blit(font.render(f"Angle: {round(Tanks_class['red'].angle)}°", True, (255, 255, 255)), (10, 50))
    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 90))

    # BLEU
    screen.blit(font.render(f"Vitesse: {round(Tanks_class['blue'].puissance)}", True, (255, 255, 255)), (1040, 10))
    screen.blit(font.render(f"Angle: {round(Tanks_class['blue'].angle)}°", True, (255, 255, 255)), (1040, 50))
    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (1040, 90))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
