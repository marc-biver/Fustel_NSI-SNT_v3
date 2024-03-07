def Verif_Doublons_Optim(liste):
    '''
    Fonction qui prend en entrée une liste quelconque et qui vérifie qu'elle ne contient pas de doublon.
    Elle renvoie True si elle en trouve au moins un, False sinon.
    '''
    # On commence par parcourir la totalité de la liste
    for i in range(len(liste)):
        # Pour chaque élément liste[i] on le compare avec tous ceux qui suivent 
        for j in range(i + 1, len(liste)):
            if liste[i] == liste[j]:
                # Si on a trouvé un doublon, on s'arrête
                return True
    # Si on a atteint ce point c'est qu'on a fait toutes les comparaisons et qu'on n'a trouvé aucun doublon.
    return False
