'''
Correction de l'activité Capytale2 "Analyse de données CSV"
Auteur: Marc Biver
'''

def Sep():
    '''
    Fonction affichant une ligne à l'écran pour séparer
    visuellement les réponses aux questions
    Note: "\n" = passage à la ligne
    '''
    print("\n###########################################\n")

def PrtQ(num):
    '''
    Fonction qui affiche simplement le numéro de la question en cours,
    qu'elle prend en entrée.
    '''
    print("Question(s):", num)
    print("\n")

import csv # On va évidemment utiliser le module CSV

# Question 1 -  ouverture en lecture du fichier
PrtQ(1)
fichier = open("DataLycees2022.csv","r",encoding = "utf-8")
print("Fichier ouvert")
Sep()

# Question 2 -  chargement du contenu du fichier dans une
#               liste de dictionnaires
PrtQ(2)
table = list(csv.DictReader(fichier))
print("Fichier chargé")
Sep()

# Question 3.1 - affichage 5 premières lignes du fichier
PrtQ("3.1")
for i in range(5):
    print(table[i])
print("5 premières lignes du fichier")
Sep()

#Question 3.2 - affichage des lignes 1500 à 1510
PrtQ("3.2")
for i in range(1499,1510):
    print(table[i])
print("Lignes 1500 à 1510 du fichier")
Sep()

#Question 3.3 - nombre de lignes du fichier (hors ligne de titres de colonnes)
PrtQ("3.3")
print("Nombre lignes du fichier:", len(table))
Sep()

#Question 4.1 - département de commune d'Ambert
PrtQ("4.1")
for i in range(len(table)):
    if table[i]['commune']=='AMBERT':
        print("Département commune Ambert:", table[i]['departement'])
Sep()

#Question 4.2 - nombre de lycées en Nouvelle Aquitaine
PrtQ("4.2")
a = 0
for i in range(len(table)):
    if table[i]['region_academique']=='NOUVELLE-AQUITAINE':
        a+=1
print("Nombre lycées en Nouvelle-Aquitaine:", a)
Sep()

#Question 4.3 & 4.4 - recherche de noms de lycées
PrtQ("4.3 & 4.4")
def cherchelycee(patro, table):
    '''
    Fonction qui cherche dans la table dans la colonne patronyme le nom passé en argument.
    Si elle le trouve elle renvoie le nom de la commune.
    Dans le cas contraire elle renvoie le message "Pas trouvé!)
    '''
    trouve = False
    for i in range (len(table)):
        if table[i]['patronyme'] == patro:
            return(table[i]['commune'])
            trouve = True

    if trouve == False:
        return('Pas trouvé!')
print("Commune lycée Docteur Dupont:", cherchelycee("DOCTEUR DUPONT", table))
print("Commune lycée Docteur Dupont:", cherchelycee("DOCTEUR KOEBERLE", table))
Sep()

#Questions 5.1, 5.2, 5.3 - élèves en 2nde GT au lycée général de Uturoa
PrtQ("5.1, 5.2, et 5.3")
for i in range(len(table)):
    if table[i]['commune'] =='UTUROA' and \
       table[i]['denomination_principale'] =='LYCEE GENERAL' :
        Nb2nde = int(table[i]['2ndes_gt'])
        NbFilles = int(table[i]['2ndes_gt_filles'])
print("Nombre élèves 2ndeGT Lycée Général Uturoa:", Nb2nde)
print("Nombre filles 2ndeGT Lycée Général Uturoa:", NbFilles)
PropFilles = round(NbFilles / Nb2nde * 100, 2)
print("Proportion filles 2ndeGT Lycée Général Uturoa:", PropFilles, "%")
Sep()

#Question 6.1 - Validation des données de la table
# Remarque: pour un problème d'encodage, le titre de la première colonne
# ("rentrée scolaire") ne passe pas tel quel - il faut utiliser "\ufeffrentree_scolaire"
# à la place.
# (pour vraiment résoudre le problème il aurait fallu utiliser l'encodage
# "utf-8-sig" au moment de la lecture du fichier - mais on ne va pas
# rentrer là-dedans ici.
PrtQ("6.1")
def validation_table(table_donnees):
    '''
    Fonction de validation des données de rentrées scolaires des lycées de France.
    Concrètement, conversion au format entier de toutes les données entières.
    '''
    for i in range(len(table_donnees)):
        table_donnees[i]['\ufeffrentree_scolaire'] = int(table_donnees[i]['\ufeffrentree_scolaire'])
        table_donnees[i]['nombre_d_eleves'] = int(table_donnees[i]['nombre_d_eleves'])
        table_donnees[i]['2ndes_gt'] = int(table_donnees[i]['2ndes_gt'])
        table_donnees[i]['2ndes_gt_filles'] = int(table_donnees[i]['2ndes_gt_filles'])
        table_donnees[i]['2ndes_gt_garcons'] = int(table_donnees[i]['2ndes_gt_garcons'])
        table_donnees[i]['2ndes_gt_lv1_allemand'] = int(table_donnees[i]['2ndes_gt_lv1_allemand'])
        table_donnees[i]['2ndes_gt_lv1_anglais'] = int(table_donnees[i]['2ndes_gt_lv1_anglais'])
        table_donnees[i]['2ndes_gt_lv1_espagnol'] = int(table_donnees[i]['2ndes_gt_lv1_espagnol'])
    return table_donnees

table = validation_table(table) # donc à partir de maintenant toutes les données seront au bon format
print("Données de la table validées")
Sep()

#Question 6.2 - pourcentage de filles en 2nde GT
PrtQ("6.2")
def pourcent_fille(table, deno, patro):
    '''
    Fonction qui prend en entrée une table de données, la dénomination principale
    et le patronyme d'un lycée et qui renvoie le pourcentage de filles en 2nde GT
    '''
    nb2nde = 0
    nbFilles = 0
    for i in range(len(table)):
        if table[i]['denomination_principale'] == deno and table[i]['patronyme'] == patro:
            nbFilles +=  table[i]['2ndes_gt_filles']
            nb2nde = table[i]['2ndes_gt'] # pas besoin de int() parce que la validation des données a été faite
    return(round((nbFilles/nb2nde)*100,2))
# 2 tests de cette fonction:
print("Pourcentage de filles en 2nde au Lycée Général Lamartine", \
      pourcent_fille(table, "LYCEE GENERAL", "LAMARTINE"), "%")
print("Pourcentage de filles en 2nde au Lycée Polyvalent Geneviève Vincent", \
      pourcent_fille(table,'LYCEE POLYVALENT','GENEVIEVE VINCENT'), "%")
Sep()


#Question 7.1 - nombre d'élèves en 2ndeGT en France à la rentrée 2022
PrtQ("7.1")
somme = 0 
for i in range(len(table)):
    if table[i]['\ufeffrentree_scolaire'] == 2022:
        somme += table[i]['2ndes_gt']
print("Nombre total d'élèves en 2ndeGT en France à la rentrée 2022:", somme)
Sep()

#Question 7.2 - pourcentage du nombre total d'élèves en établissement privé et ont choisi allemand comme LV1
PrtQ("7.2")
nb2nde = 0
nbPriveAllemand = 0
for i in range(len(table)):
    nb2nde += table[i]['2ndes_gt']
    if table[i]['secteur'] == 'PRIVE':
        nbPriveAllemand += table[i]['2ndes_gt_lv1_allemand']

pct = round((nbPriveAllemand/nb2nde)*100,2)
print("% d'élèves en établissement privé et ont choisi allemand comme LV1:", pct, "%")
Sep()

#Question 7.3 - pourcentage du nombre total d'élèves qui sont en établissement privé, ont choisi allemand comme LV1, et sont des filles? 
PrtQ("7.3")
print("Cette question était un piège - voir le commentaire dans le code du corrigé")
# Les données ne permettent pas de répondre à cette question: par établissement on connait le nombre de filles,
# et on connait le nombre d'élèves qui ont pris allemand comme LV1, mais on ne peut pas connaitre l'intersection
# des deux - combien, parmi les filles, ont fait ce choix de LV1.
# Il était donc impossible de répondre à la question.
Sep()

#Question 7.4 - pourcentage moyen de filles en 2nde GT en établissement privé? En établissement public? Au total?
PrtQ("7.4")
# Cette question est un peu plus complexe puisqu'on parle de pourcentage moyen - ce qui en soit est ambigu.
# On va donc calculer ici deux choses pour les comparer:
# Le pourcentage moyen (donc la somme de toutes les filles sur la somme de tous les élèves) et la
# moyenne des pourcentages (chaque pourcentage de chaque établissement étant pris dans une liste dont
# on va faire la moyenne).
# Pour rendre le code lisible on va utiliser un dictionnaire de valeurs
sommes = dict()
sommes['2nde-Public'] = 0 # Nombre d'élèves en 2nde dans le public
sommes['2nde-Prive'] = 0 # Nombre d'élèves en 2nde dans le privé
sommes['Filles-Public'] = 0 # Nombre d'élèves filles dans le public
sommes['Filles-Prive'] = 0 # Nombre d'élèves filles dans le privé
sommes['Moy-Public'] = 0 # Somme des moyennes de filles par établissement dans le public
sommes['Nb-Public'] = 0 # Nombre d'établissements publics considérés (pour faire la moyenne de moyennes)
sommes['Moy-Prive'] = 0 # Somme des moyennes de filles par établissement dans le privé
sommes['Nb-Prive'] = 0 # Nombre d'établissements publics considérés (pour faire la moyenne de moyennes)

for i in range(len(table)):
    # On ne regarde que les lycées qui ont des élèves en seconde (sinon on fera des divisions par zéro):
    if table[i]['2ndes_gt'] > 0:
        if table[i]['secteur'] == "PUBLIC":
            sommes['2nde-Public'] += table[i]['2ndes_gt']
            sommes['Filles-Public'] += table[i]['2ndes_gt_filles']
            sommes['Nb-Public'] += 1 # On ajoute un établissement seulement
            sommes['Moy-Public'] += table[i]['2ndes_gt_filles'] / table[i]['2ndes_gt']
        else:
            sommes['2nde-Prive'] += table[i]['2ndes_gt']
            sommes['Filles-Prive'] += table[i]['2ndes_gt_filles']
            sommes['Nb-Prive'] += 1 # On ajoute un établissement seulement
            sommes['Moy-Prive'] += table[i]['2ndes_gt_filles'] / table[i]['2ndes_gt']

# On a maintenant toutes les informations qu'il nous faut - faisons les calculs de nos résultats:
# Pourcentages moyens pour commencer
PctMoyPub = round(sommes['Filles-Public'] / sommes['2nde-Public'] * 100, 2)
PctMoyPrv = round(sommes['Filles-Prive'] / sommes['2nde-Prive'] * 100, 2)
PctMoyTot = round((sommes['Filles-Public'] + sommes['Filles-Prive']) / (sommes['2nde-Public'] + sommes['2nde-Prive']) * 100, 2)
# Moyennes de pourcentage ensuite
MoyMoyPub = round(sommes['Moy-Public'] / sommes['Nb-Public'] * 100, 2)
MoyMoyPrv = round(sommes['Moy-Prive'] / sommes['Nb-Prive'] * 100, 2)
MoyMoyTot = round((sommes['Moy-Public'] + sommes['Moy-Prive']) / (sommes['Nb-Public'] + sommes['Nb-Prive']) * 100, 2)

# Il nous reste maintenant à afficher tout ça dans un beau tableau - même si j'ai conscience qu'on n'a
# pas encore vu cette syntaxe de print.
# En-têtes
header = f"{' ':<25} {'Public':<10} {'Privé':<10} {'Total':<10}"
# Lignes de données
row1 = f"{'Pourcentage moyen':<25} {PctMoyPub:<10} {PctMoyPrv:<10} {PctMoyTot:<10}"
row2 = f"{'Moy. de pourcentages':<25} {MoyMoyPub:<10} {MoyMoyPrv:<10} {MoyMoyTot:<10}"
# Affichage du tableau
print(header)
print(row1)
print(row2)
Sep()
# Et c'est fini!
print("==================== FIN ====================")
