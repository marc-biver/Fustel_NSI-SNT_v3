def TSP(Villes, Distances, Depart):
    '''
    Fonction de résolution du problème du voyageur de commerce par une approche gloutonne.
    Entrée: une liste de villes (leurs noms); une liste de listes représentant la matrice des distances entre les villes; le nom de la ville point de départ.
    Sortie: une liste contenant le parcours complet, sous forme d'une succession de noms de villes.
    '''
    
    # Récupération de l'indice de la ville de départ
    idDepart = Villes.index(Depart)

    # Initialisation du parcours: ville de départ
    Parcours = [idDepart]

    # Positionnement de la ville courante: ville de départ
    VilleCourante = idDepart

    # Boucle principale sur la longueur du parcours
    while len(Parcours) < len(Villes):
        # Distance minimale initialisée à 0
        CurMin = 0

        # Parcours de toutes les distances depuis la ville courante
        for i in range(len(Distances[VilleCourante])):
            # On ne considère que les villes non déjà sur le parcours
            if i not in Parcours:
                # On vérifie si soit la distance minimale n'existe pas encore soit la distance considérée lui est inférieure
                if CurMin == 0 or Distances[VilleCourante][i] < CurMin:
                    # On a trouvé une prochaine ville meilleure que la précédente
                    CurMin = Distances[VilleCourante][i]
                    ProchVille = i

        # On a tout parcouru, on connaît donc la prochaine ville du parcours            
        Parcours.append(ProchVille)
        # Elle devient la ville courante
        VilleCourante = ProchVille

    # On a fini le parcours, on rajoute le point de départ pour que ce soit une boucle
    Parcours.append(idDepart)
    
    # Pour renvoyer le parcours avec les noms de ville on traduit à présent indices en utilisant la table Villes
    for i in range(len(Parcours)):
        Parcours[i] = Villes[Parcours[i]]
        
    return Parcours
