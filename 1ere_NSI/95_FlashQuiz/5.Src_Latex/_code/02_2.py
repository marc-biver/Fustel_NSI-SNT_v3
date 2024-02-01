LstNoms = [
    {'prenom': 'Fatima', 'nom': 'Diallo'},
    {'prenom': 'Lucas', 'nom': 'Fernandez'},
    ]

trouve = False
cherche = input("Quel nom? ")
for i in range(len(LstNoms)):
    if LstNoms[i]['nom'] == cherche:
        print("Son prénom est", LstNoms[i]['prenom'])
        trouve = True

if trouve == False:
    print("Absent de la liste!")
