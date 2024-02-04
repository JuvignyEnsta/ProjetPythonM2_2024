import numpy as np
import pygame 

NORTH = 1
EAST  = 2
SOUTH = 4
WEST  = 8

# Création à la main d'un "mini"-labyrinthe
laby = np.array([[EAST+SOUTH, WEST+SOUTH],
                 [NORTH, NORTH]])

pygame.init()

# Création de la fenêtre d'affichage (résolution 16x16 ici)
screen = pygame.display.set_mode((16,16))

# Chargement des différentes cases possibles :
img = pygame.image.load("cases.png").convert_alpha()
# qu'on découpe en plusieurs images (une par configuration) :
cases_spr = []
for i in range(0, 128, 8):
    cases_spr.append(pygame.Surface.subsurface(img, i, 0, 8, 8))

# Création de l'image du labyrinthe :
maze_img = pygame.Surface((8*laby.shape[1], 8*laby.shape[0]), flags=pygame.SRCALPHA)
for i in range(laby.shape[0]):
    for j in range(laby.shape[1]):
        maze_img.blit(cases_spr[laby[i, j]], (j*8, i*8))

# Remplit l'écran avec du blanc
screen.fill((255,255,255))
# On affiche l'image du labyrinthe par dessus
screen.blit(maze_img, (0,0))

# Mise à jour de l'écran
pygame.display.update()

# Boucle où on attend qu'on quitte l'écran en appuyant sur la croix pour quitter.
loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
# On quitte le contexte pygame
pygame.quit()
