LstSujets = [
    {'sujet': 'Python', 'difficulte': 2},
    {'sujet': 'Algorithmique', 'difficulte': 4},
    {'sujet': 'Représentation données', 'difficulte': 3}
    ]

def SujetsFaciles(seuil, lst):
    ''' Renvoie la liste des sujets qui ont une difficulté < seuil '''
    resultat = []
    for i in range(len(lst)):
        if lst[i]['difficulte'] < seuil:
            resultat.append(lst[i]['sujet'])
    return resultat
