import pygame
from pygame.locals import *

pygame.init()

# On crée une fenêtre beaucoup plus large pour laisser la place au ballon
fenetre = pygame.display.set_mode((700, 480))
fenetre.fill([10,186,181])

# On démarre le mécanisme de contrôle des FPS
clock = pygame.time.Clock()

# On charge l'image et on la redimensionne
balle = pygame.image.load("ballon.png")
balle = pygame.transform.scale(balle, (60,60))

# On place le ballon tout à gauche de la fenêtre et on le dessine
position_balle = balle_x, balle_y = 0, 210
fenetre.blit(balle, position_balle)

continuer = True
while continuer:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            continuer = False
    # On augmente l'abscisse du ballon
    balle_x += 5
    position_balle = balle_x, balle_y

    # On dessine le ballon à sa nouvelle position
    fenetre.blit(balle, position_balle)
    pygame.display.flip()
    
    # On demande à pygame de réguler la vitesse de la boucle
    clock.tick(60)

pygame.quit()
