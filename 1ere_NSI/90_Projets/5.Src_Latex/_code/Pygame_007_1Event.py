import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
Largeur_Fenetre = 640
Hauteur_Fenetre = 480
fenetre = pygame.display.set_mode((Largeur_Fenetre, Hauteur_Fenetre))
fenetre.fill([10,186,181])

# On charge l'image et on la redimensionne
balle = pygame.image.load("ballon.png")
balle = pygame.transform.scale(balle, (60,60))

# On place le rectangle de la balle, puis son image dessus
ballrect = balle.get_rect(topleft = (0,210))
fenetre.blit(balle, ballrect)

# Vitesse initialisée à 0 (donc ballon immobile)
vitesse = [0,0]

continuer = True
while continuer:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            continuer = False
        # Gestion d'un appui sur la barre d'espace
        if evenement.type == KEYDOWN:
            if evenement.key == K_SPACE:
                vitesse = [5,0]

    # La balle bouge à la vitesse spécifiée
    ballrect = ballrect.move(vitesse)

    # On vide la fenêtre pour effacer la trainée
    fenetre.fill([10,186,181])

    # On dessine le ballon à sa nouvelle position
    fenetre.blit(balle, ballrect)
    pygame.display.flip()
    
    # On demande à pygame de réguler la vitesse de la boucle
    clock.tick(60)

pygame.quit()
