import pygame

pygame.mixer.init()

class Son:
    def __init__(self):
        # Charge les sons
        self.shoot = pygame.mixer.Sound("Sounds/shoot.wav")
        self.hit = pygame.mixer.Sound("Sounds/hit.wav")
        self.explosion = pygame.mixer.Sound("Sounds/explosion.wav")

        # Réglage volume (0.0 → 1.0)
        self.shoot.set_volume(0.5)
        self.hit.set_volume(0.5)
        self.explosion.set_volume(0.7)

    def play_shoot(self):
        self.shoot.play()

    def play_hit(self):
        self.hit.play()

    def play_explosion(self):
        self.explosion.play()
