def EltPondere(lst_notes, indice):
    '''
    Fonction qui prend en entrée une liste de notes et un indice dans cette liste et qui renvoie la valeur pondérée de cette note (donc sa valeur divisée par le nombre de notes).
    '''
    res = lst_notes[indice] / len(lst_notes)
    return res
