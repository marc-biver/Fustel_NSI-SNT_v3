import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))
fenetre.fill([10,186,181])

# On charge l'image et on la redimensionne
balle = pygame.image.load("ballon.png")
balle = pygame.transform.scale(balle, (60,60))

# On la place dans la fenêtre et on la dessine
position_balle = (290, 210)
fenetre.blit(balle, position_balle)

continuer = True
while continuer:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            continuer = False
    pygame.display.flip()

pygame.quit()
