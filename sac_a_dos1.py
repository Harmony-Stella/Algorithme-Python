def sac_a_dos(objets, poids_max, critere_local):
    if critere_local == "valeur":
        # Trier les objets par ordre décroissant de valeur
        objets_tries = sorted(objets, key=lambda x: x[1], reverse=True)
    elif critere_local == "poids":
        # Trier les objets par ordre croissant de poids
        objets_tries = sorted(objets, key=lambda x: x[0])
    elif critere_local == "masse":
        # Trier les objets par ordre décroissant de rapport valeur/poids
        objets_tries = sorted(objets, key=lambda x: x[1]/x[0], reverse=True)
        
    poids_total = 0
    valeur_totale = 0
    objets_selectionnes = []
    
    # Parcourir les objets triés et sélectionner ceux qui peuvent être ajoutés au sac à dos
    for objet in objets_tries:
        if poids_total + objet[0] <= poids_max:
            objets_selectionnes.append(objet)
            poids_total += objet[0]
            valeur_totale += objet[1]
    
    return objets_selectionnes, valeur_totale, poids_total


# Poids initial du sac à dos
poids_max = 30

# Demander à l'utilisateur de saisir le nombre d'objets dont il dispose
demande = int(input("Entrez le nombre d'objets dont vous disposez : "))
print()  # Ligne vide pour plus de lisibilité

# Demander à l'utilisateur de saisir les informations relatives à chaque objet
objets = []
for i in range(demande):
    masse = float(input("Entrez la masse de l'objet {} en kg : ".format(i+1)))
    print()  # Ligne vide pour plus de lisibilité
    valeur = float(input("Entrez la valeur de l'objet {} en euros : ".format(i+1)))
    print()  # Ligne vide pour plus de lisibilité
    objets.append((masse, valeur))

# Appliquer l'algorithme glouton pour chaque critère local
for critere_local in ["valeur", "poids", "masse"]:
    objets_selectionnes, valeur_totale, poids_total = sac_a_dos(objets, poids_max, critere_local)
    print()  # Ligne vide pour plus de lisibilité
    print("Critère local : {}".format(critere_local))
    print("Objets sélectionnés : {}".format(objets_selectionnes))
    print("Valeur totale : {} euros".format(valeur_totale))
    print("Poids total : {} kg".format(poids_total))
    print()  # Ligne vide pour plus de lisibilité