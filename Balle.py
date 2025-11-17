import pygame           # Programme Balle.py
import random           # On importe les bibliothèques

BLACK = (0, 0, 0)       # On définit des constantes utiles plus tard
WHITE = (255, 255, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 20

def bouger():
    global x,y, vitesseX, vitesseY
    x = x + vitesseX    # modifie la position de la balle
    y = y + vitesseY

def rebondir():
    global x,y, vitesseX, vitesseY
    if (x > SCREEN_WIDTH-20 or x < 20): # test si collision sur les bords
        vitesseX = vitesseX * -1        # alors change de sens
    if (y > SCREEN_HEIGHT-20 or y < 20):
        vitesseY = vitesseY * -1

def afficher():
    global screen, couleur, size
    pygame.draw.circle(screen, couleur, [x, y], BALL_SIZE) # affiche la balle

def main():             # Entrée du programme
    pygame.init()       # Initialisation de la bibliothèque PyGame

    couleur = WHITE     # Variable de la couleur de la balle

    x = SCREEN_WIDTH//2   # Calcul du centre de la fenêtre (Résultat en entier)
    y = SCREEN_HEIGHT//2
    vitesseX = 2 + random.randint(-1,1)   # Fixe une vitesse aléatoire
    vitesseY = 2 + random.randint(-1,1)

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]    # Variable taille d'écran
    screen = pygame.display.set_mode(size)  # Création de la fenêtre
    pygame.display.set_caption("Rebond d'une balle") # Nom de la fenêtre
    clock = pygame.time.Clock()     # Variable de controle du nombre d'images/s
    fin = False               # Variable de détection de fin



    # -------- Boucle du programme
    while not fin:
        # --- Test du clip de fermeture de la fenêtre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        screen.fill(BLACK)  # efface en noir la fenêtre

        bouger()

        rebondir()

        afficher()

        clock.tick(60)          # ralenti l'affichage
        pygame.display.flip()   # mise à jour de l'affichage

    pygame.quit()               # fermeture de la fenêtre


if __name__ == "__main__":
    main()