import pygame
import math
from colorama import Fore, Style, init

import Function.core.Balle as Balle
import Function.core.Tank as Tank
import Function.core.Cible as Cible
import Function.core.Particule as Particule
from Function.core.Terrain import Terrain
from Function.core.son import Son
from Function.core.Cloud import Cloud
from Function.core.Life import Life


pygame.init()  # Initialiser Pygame

class GameEnv:
    def __init__(self, visualize=True):
        self.state = None
        self.visualize = visualize
        # --- Initialisation son ---
        self.sons = Son(color_tank_list[:nb_tank])

        self.Terrain_class = Terrain(self.width, self.height)

        # Créer des nuages
        self.clouds = [Cloud(self.width, self.height) for _ in range(5)]   # 5 nuages

        self.balles = []
        self.particules = []
        if self.visualize:
            self.screen = pygame.display.set_mode((self.width, self.height))

        
        self.max_vitesse = 35

        self.max_puissance = 35

    def reset(self):

        self.Tanks_class = {}
        # --- Création des tanks ---
        for i in range(self.nb_tank):
            x_tank_spawn = (i + 1) * (self.width / (self.nb_tank + 1))
            x_tank_spawn -= 42.5
            color = self.color_tank_list[i]

            self.Tanks_class[color] = Tank.Tank(
                self.width,
                self.height,
                x_tank_spawn,
                color
            )
        self.Terrain_class.generate_terrain()
        return self.state

    def Episode(self):
        pass

    def step(self, action):
        if self.visualize:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        # --------------------- UPDATE BALLES ---------------------
        for balle in list(self.balles):
            position_disparition = balle.update(self.Terrain_class.array_terrain)

            if position_disparition:
                #Terrain_class.change_terrain_at(balle.x, balle.y, radius=16)
                balle.owner.can_shoot = True

                # particules explosion
                for _ in range(100):
                    self.particules.append(
                        Particule.Particule(position_disparition[0], position_disparition[1], balle.color)
                    )

        # --------------------- LIMITE DU TERRAIN ---------------------
        for tank_name in self.Tanks_class:
            if self.Tanks_class[tank_name].x < 0:
                self.Tanks_class[tank_name].x = 0
            if self.Tanks_class[tank_name].x > self.width - ( self.Tanks_class[tank_name].draw_width + 1 ):
                self.Tanks_class[tank_name].x = self.width - ( self.Tanks_class[tank_name].draw_width +1 )
        for cloud in self.clouds:
            cloud.update()


        # --------------------- DESSIN TANKS ---------------------
        for tank_name in self.Tanks_class:
            self.Tanks_class[tank_name].draw(self.screen, self.Terrain_class.array_terrain)

        # --------------------- DESSIN BALLES ---------------------
        for balle in list(balles):
            if balle.visible:
                balle.draw(self.screen)
            else:
                self.balles.remove(balle)
                continue

            # ------------------ COLLISION BALLE / TANK ------------------
            for name, tank in self.Tanks_class.items():

                if tank == balle.owner:
                    continue

                if tank.hit(balle):

                    print(getattr(Fore, name.upper()) + f"{name} touché !" + Style.RESET_ALL)

                    tank.hp -= 1

                    self.sons.play_hit()

                    if tank.hp <= 0:
                        print(getattr(Fore, name.upper()) + f"{name} LOSE !" + Style.RESET_ALL)

                    balle.owner.can_shoot = True

                    balle.visible = False
                    self.balles.remove(balle)
                    break
    
    def take_action(self, action):
        return self.step(action)
    
    def get_human_action(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.sons.play_turret("red")
            self.Tanks_class["red"].angle = min(180, self.Tanks_class["red"].angle + 0.8)
        elif keys[pygame.K_e]:
            self.sons.play_turret("red")
            self.Tanks_class["red"].angle = max(0, self.Tanks_class["red"].angle - 0.8)
        else:
            self.sons.turret_playing["red"] = False

        if keys[pygame.K_s]:
            self.Tanks_class["red"].puissance = max(5, self.Tanks_class["red"].puissance - 0.3)
        if keys[pygame.K_z]:
            self.Tanks_class["red"].puissance = min(self.max_vitesse, self.Tanks_class["red"].puissance + 0.3)

        if keys[pygame.K_q]:
            self.Tanks_class["red"].x -= self.Tanks_class["red"].vitesse
        if keys[pygame.K_d]:
            self.Tanks_class["red"].x += self.Tanks_class["red"].vitesse

        if keys[pygame.K_f] and self.Tanks_class["red"].can_shoot:
            cannon_end_x, cannon_end_y = self.Tanks_class["red"].draw(self.screen, self.Terrain_class.array_terrain)
            angle = math.radians(self.Tanks_class["red"].angle) + math.radians(self.Tanks_class["red"].z_rotation)
            angle = math.degrees(angle)
            self.sons.play_shoot()
            self.balles.append(Balle.Balle(
                self.width, self.height, cannon_end_x, cannon_end_y,
                5, angle, self.Tanks_class["red"].puissance,
                self.Tanks_class["red"].vitesse * self.Tanks_class["red"].direction,
                owner=self.Tanks_class["red"], color_tank ="red"
                ))
            self.Tanks_class["red"].can_shoot = False

        # ------------------ CONTROLES TANK BLEU ------------------
        if keys[pygame.K_i]:
            self.sons.play_turret("blue")
            self.Tanks_class["blue"].angle = min(180, self.Tanks_class["blue"].angle + 0.8)
        elif keys[pygame.K_p]:
            self.sons.play_turret("blue")
            self.Tanks_class["blue"].angle = max(0, self.Tanks_class["blue"].angle - 0.8)
        else:
            self.sons.turret_playing["blue"] = False

        if keys[pygame.K_l]:
            self.Tanks_class["blue"].puissance = max(5, self.Tanks_class["blue"].puissance - 0.3)
        if keys[pygame.K_o]:
            self.Tanks_class["blue"].puissance = min(self.max_vitesse, self.Tanks_class["blue"].puissance + 0.3)

        if keys[pygame.K_k]:
            self.Tanks_class["blue"].x -= self.Tanks_class["blue"].vitesse
        if keys[pygame.K_m]:
            self.Tanks_class["blue"].x += self.Tanks_class["blue"].vitesse

        if keys[pygame.K_j] and self.Tanks_class["blue"].can_shoot:
            cannon_end_x, cannon_end_y = self.Tanks_class["blue"].draw(self.screen, self.Terrain_class.array_terrain)
            angle = math.radians(self.Tanks_class["blue"].angle) + math.radians(self.Tanks_class["blue"].z_rotation)
            angle = math.degrees(angle)
            self.sons.play_shoot()
            self.balles.append(Balle.Balle(
                self.width, self.height, cannon_end_x, cannon_end_y,
                5, angle, self.Tanks_class["blue"].puissance,
                self.Tanks_class["blue"].vitesse * self.Tanks_class["blue"].direction,
                owner=self.Tanks_class["blue"], color_tank = "blue"
            ))
            self.Tanks_class["blue"].can_shoot = False
    
    def _get_observation(self):
        pass

    def _execute_action(self, action):
        pass

    def render(self):
        # --------------------- DESSIN ÉCRAN ---------------------
        self.screen.fill((0,110,220))
        self.Terrain_class.draw_ground(self.screen)

        for cloud in self.clouds:
            cloud.draw(self.screen)
        
        # --------------------- AFFICHAGE DES VIES ---------------------
        # Tank rouge (haut gauche)
        self.life_ui["red"].draw(
            self.screen,
            self.Tanks_class["red"].hp,
            self.Tanks_class["red"].hp_max,
            x=10,
            y=600
        )

        # Tank bleu (haut droite)
        self.life_ui["blue"].draw(
            self.screen,
            self.Tanks_class["blue"].hp,
            self.Tanks_class["blue"].hp_max,
            x=self.width - (self.Tanks_class["blue"].hp_max * 50),  # auto-aligné
            y=600
        )


        # --------------------- PARTICULES ---------------------
        for particule in particules:
            particule.update(self.Terrain_class.array_terrain)
            particule.draw(self.screen)

        particules = [p for p in particules if p.lifetime > 0]

        # --------------------- UI ---------------------
        font = pygame.font.Font(None, 36)

        # ROUGE
        self.screen.blit(font.render(f"Vitesse: {round(self.Tanks_class['red'].puissance)}", True, (255, 255, 255)), (10, 10))
        self.screen.blit(font.render(f"Angle: {round(self.Tanks_class['red'].angle)}°", True, (255, 255, 255)), (10, 50))
        self.screen.blit(font.render(f"Score: {self.score}", True, (255, 255, 255)), (10, 90))

        # BLEU
        self.screen.blit(font.render(f"Vitesse: {round(self.Tanks_class['blue'].puissance)}", True, (255, 255, 255)), (1040, 10))
        self.screen.blit(font.render(f"Angle: {round(self.Tanks_class['blue'].angle)}°", True, (255, 255, 255)), (1040, 50))
        self.screen.blit(font.render(f"Score: {self.score}", True, (255, 255, 255)), (1040, 90))

        pygame.display.flip()
        self.clock.tick(60)