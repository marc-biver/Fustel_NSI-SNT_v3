def Monnaie(Montant, Coupures):
    '''
    Fonction de résolution du problème de rendu de monnaie par une approche gloutonne.
    Entrée: le Montant à rendre, une liste des coupures disponibles (en ordre décroissant).
    Sortie: une liste contenant les coupures à rendre.
    '''
    
    # Initialisation
    Rendu = []

    # Parcours des dénominations
    for denom in Coupures:
        while Montant >= denom:
            Rendu.append(denom)
            Montant -= denom

    return Rendu
