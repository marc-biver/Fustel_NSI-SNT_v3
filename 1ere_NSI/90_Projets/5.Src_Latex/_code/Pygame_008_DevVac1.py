










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
vitesse = [0, 0]

continuer = True
while continuer:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            continuer = False
        # Gestion d'un appui sur les flèches
        if evenement.type == KEYDOWN:
            if evenement.key == K_RIGHT:
                vitesse = [5,0]
            if evenement.key == K_LEFT:
                vitesse = [-5,0]
            if evenement.key == K_UP:
                vitesse = [0,-5]
            if evenement.key == K_DOWN:
                vitesse = [0,5]


    # La balle bouge à la vitesse spécifiée
    ballrect = ballrect.move(vitesse)

    # Gestion du rebond quand la balle atteint un bord:
    if ballrect.right >= Largeur_Fenetre or ballrect.left <= 0:
        # Bord latéral, c'est la vitesse en abscisse qui s'inverse
        vitesse[0] = -vitesse[0]
    if ballrect.top <= 0 or ballrect.bottom >= Hauteur_Fenetre:
        # Bord haut/bas, c'est la vitesse en ordonnée qui s'inverse
        vitesse[1] = -vitesse[1]

    # On vide la fenêtre pour effacer la trainée
    fenetre.fill([10,186,181])

    # On dessine le ballon à sa nouvelle position
    fenetre.blit(balle, ballrect)
    pygame.display.flip()
    
    # On demande à pygame de réguler la vitesse de la boucle
    clock.tick(60)

pygame.quit()
