def InverseListe(lst):
    '''
    Fonction qui prend en entrée une liste quelconque et qui renvoie la liste inversée.
    '''
    # On initialise la liste résultat - liste vide
    res = []
    # On la remplit en partant de la fin de la liste en entrée
    for i in range(len(lst)):
        res.append(lst[len(lst) - i - 1])

    return res
