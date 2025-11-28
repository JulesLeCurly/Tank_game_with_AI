import pygame

pygame.mixer.init()

class Son:
    def __init__(self):
        # Charge les sons
        self.shoot = pygame.mixer.Sound("Sounds/shoot.mp3")
        self.hit = pygame.mixer.Sound("Sounds/hit.mp3")
        self.turret = pygame.mixer.Sound("Sounds/turret-rotate.mp3")

        # Réglage volume (0.0 → 1.0)
        self.shoot.set_volume(0.5)
        self.hit.set_volume(0.4)
        self.turret.set_volume(0.2)

    def play_shoot(self):
        self.shoot.play()

    def play_hit(self):
        self.hit.play()

    def play_turret(self):
        self.turret.play()
