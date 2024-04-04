import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
Largeur_Fenetre = 700
Hauteur_Fenetre = 480
fenetre = pygame.display.set_mode((Largeur_Fenetre, Hauteur_Fenetre))
fenetre.fill([10,186,181])

# On charge l'image et on la redimensionne
balle = pygame.image.load("ballon.png")
balle = pygame.transform.scale(balle, (60,60))

# On place le rectangle de la balle, puis son image dessus
ballrect = balle.get_rect(topleft = (0,210))
fenetre.blit(balle, ballrect)

# On définit la vitesse
vitesse = [5, 0]

continuer = True
while continuer:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            continuer = False

    # La balle bouge à la vitesse spécifiée
    ballrect = ballrect.move(vitesse)

    # Gestion du rebond quand la balle atteint un bord:
    if ballrect.right >= Largeur_Fenetre or ballrect.left <= 0:
        vitesse[0] = -vitesse[0]

    # On vide la fenêtre pour effacer la trainée
    fenetre.fill([10,186,181])

    # On dessine le ballon à sa nouvelle position
    fenetre.blit(balle, ballrect)
    pygame.display.flip()
    
    # On demande à pygame de réguler la vitesse de la boucle
    clock.tick(60)

pygame.quit()
