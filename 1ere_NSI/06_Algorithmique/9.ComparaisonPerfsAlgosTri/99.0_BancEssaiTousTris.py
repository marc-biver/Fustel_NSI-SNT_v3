# On crée ici plusieurs tableaux en utilisant la syntaxe par compréhension
# (on la reverra plus en détails plus tard)

# On va utiliser le module random pour générer des nombres au hasard
import random as r
import time as t
import copy as c
import csv
from datetime import datetime

# Les trois fonctions de tri
def TriSel(tab):
    '''
    Fonction qui effectue le tri par sélection de la table passée en entrée.
    '''
    n = len(tab)
    for p in range(n-1):
        pmin = p
        for j in range(p + 1, n):
            if tab[j] < tab[pmin]:
                pmin = j
        tab[pmin], tab[p] = tab[p], tab[pmin]
    return tab

def TriIns(tab):
    '''
    Fonction qui effectue le tri par insertion de la liste passée en entrée.
    '''
    n = len(tab)
    for i in range(1, n):
        p = i
        temp = tab[i]
        while p > 0 and tab[p-1] > temp:
            tab[p] = tab[p-1]
            p -= 1
        tab[p] = temp
    return tab

def TriBulles(liste):
    '''
    Fonction qui effectue le tri par permutations de la liste passée en entrée.
    '''
    n = len(liste)
    for i in range(n):
        for j in range(n-1):
            if liste[j] > liste[j+1]:
                # Cette syntaxe permet d'affecter deux variables simultanément et donc de ne pas passer par une variable intermédiaire
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste


# Le banc d'essai lui-même
def BancEssaiTri(TypeTri, nbit):
    '''Fonction générique qui marche sur les trois types de tris'''
    NB_IT = nbit
    DureesTours = []
    DD = t.time()

    # On construit les tableaux
    # T1: 20.000 nombres entiers compris entre 0 et 100.000, dans un ordre complètement aléatoire
    T1 = [r.randint(0,1000000) for i in range(20000)]
    # T2: les nombres 0 à 19.999, dans l'ordre croissant
    T2 = [i for i in range(20000)]
    # T3: tableau en deux moitiés:
    #       - Indices 0 à 9.999 (Ta): les nombres de 0 à 9.999, dans l'ordre
    #       - Indices 10.000 à 19.999 (Tb): 10.000 nombres au hasard, en ordre aléatoire
    Ta = [i for i in range(10000)]
    Tb = [r.randint(0,1000000) for i in range(10000)]
    T3 = Ta + Tb
    # T3bis: les mêmes deux moitiés que T3, mais dans l'ordre inverse (Tb puis Ta)
    T3bis = Tb + Ta
    # T4: le même tableau que T2, mais en ordre exactement inverse (19.999 à 0, dans l'ordre)
    T4 = [19999 - i for i in range(20000)]

    # Versions de référence pour les réutiliser
    T1r = c.deepcopy(T1)
    T2r = c.deepcopy(T2)
    T3r = c.deepcopy(T3)
    T3br = c.deepcopy(T3bis)
    T4r = c.deepcopy(T4)
    tp1 = []
    tp2 = []
    tp3 = []
    tp3b = []
    tp4 = []
    # Exécution du tri demandé sur chacun de ces tableaux
    for i in range(NB_IT):
        
        Dcurdeb = t.time()
        deb1 = t.time() 
        if TypeTri == "sel":
            x = TriSel(T1)
        elif TypeTri == "ins":
            x = TriIns(T1)
        elif TypeTri == "bul":
            x = TriBulles(T1)
        else:
            return(-1)
        fin1 = t.time()
        tp1.append(fin1 - deb1)
        deb2 = t.time()
        if TypeTri == "sel":
            x = TriSel(T2)
        elif TypeTri == "ins":
            x = TriIns(T2)
        elif TypeTri == "bul":
            x = TriBulles(T2)
        fin2 = t.time()
        tp2.append(fin2 - deb2)
        deb3 = t.time()
        if TypeTri == "sel":
            x = TriSel(T3)
        elif TypeTri == "ins":
            x = TriIns(T3)
        elif TypeTri == "bul":
            x = TriBulles(T3)
        fin3 = t.time()
        tp3.append(fin3 - deb3)
        deb3b = t.time()
        if TypeTri == "sel":
            x = TriSel(T3bis)
        elif TypeTri == "ins":
            x = TriIns(T3bis)
        elif TypeTri == "bul":
            x = TriBulles(T3bis)
        fin3b = t.time()
        tp3b.append(fin3b - deb3b)
        deb4 = t.time()
        if TypeTri == "sel":
            x = TriSel(T4)
        elif TypeTri == "ins":
            x = TriIns(T4)
        elif TypeTri == "bul":
            x = TriBulles(T4)
        fin4 = t.time()
        tp4.append(fin4 - deb4)
        # On remet tout le monde à sa place
        T1 = c.deepcopy(T1r)
        T2 = c.deepcopy(T2r)
        T3 = c.deepcopy(T3r)
        T3bis = c.deepcopy(T3br)
        T4 = c.deepcopy(T4r)
        # Fin d'un tour de boucle
        Dcurfin = t.time()
        Dcur = round(Dcurfin - Dcurdeb, 2)
        #Enregistre donc juste des marqueurs tous les 10 pour savoir où on en est
        #print(i+1, "tour(s) fait(s); durée:",Dcur,"secondes.")
        if i % 10 == 0:
            print(i+1, "tours faits sur", NB_IT, "...")
        DureesTours.append(Dcur)

    # Calcul des sommes
    nb = len(tp1)
    sm1 = sum(tp1)
    sm2 = sum(tp2)
    sm3 = sum(tp3)
    sm3b = sum(tp3b)
    sm4 = sum(tp4)

    # Calcul des moyennes
    tp1s = round(sm1 / nb, 2)
    tp2s = round(sm2 / nb, 2)
    tp3s = round(sm3 / nb, 2)
    tp3bs = round(sm3b / nb, 2)
    tp4s = round(sm4 / nb, 2)

    #Affichage
    print(f"Durées moyennes de tri par sélection sur {nb} exécutions")
    print("pour des tableaux de 20.000 éléments:")
    print("===============================================================")
    print(f"Temps T1 (tableau non ordonné)              : {tp1s} secondes")
    print(f"Temps T2 (tableau dans l'ordre ascendant)   : {tp2s}  secondes")
    print(f"Temps T3 (moitié ordonné, moitié non)       : {tp3s} secondes")
    print(f"Temps T3bis (moitié non, moitié ordonné)    : {tp3bs} secondes")
    print(f"Temps T4 (tableau dans l'ordre descendant)  : {tp4s} secondes")

    # Et la totale
    FF = t.time()
    DD = round(FF - DD, 2)
    print(f"TOTAL: {DD} secondes")

    # Ecriture des dureesIndividuelles
    a = t.time()
    date_heure = datetime.fromtimestamp(a)
    format_date_heure = date_heure.strftime("%Y%m%d%H%M%S")
    NomFic = format_date_heure + "_DureesTri_" + TypeTri + ".csv"
    Hdrs = ["Tout", "T1", "T2", "T3", "T3bis", "T4"]
    with open(NomFic, 'w', newline='') as fichier:
        # Créer un objet writer
        wrt = csv.writer(fichier, delimiter=';')
        wrt.writerow(Hdrs)
        # On écrit:
        for elt, elt1, elt2, elt3, elt3b, elt4 in zip(DureesTours, tp1, tp2, tp3, tp3b, tp4):
            wrt.writerow([elt, elt1, elt2, elt3, elt3b, elt4])

BancEssaiTri("bul",100)
BancEssaiTri("sel",200)
BancEssaiTri("ins",200)
