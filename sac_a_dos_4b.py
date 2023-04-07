# # Questrion 1
def sac_a_dos(masse_max, objets):
    # tri des objets par ordre décroissant de valeur
    objets_tries = sorted(objets, key=lambda x: x[0], reverse=True)
    
    poids_total = 0
    valeur_totale = 0
    objets_selectionnes = []
    
    # Parcourir les objets triés et sélectionner ceux qui peuvent être ajoutés au sac à dos
    for objet in objets_tries:
        if poids_total + objet[1] <= masse_max:
            objets_selectionnes.append(objet)
            poids_total += objet[1]
            valeur_totale += objet[0]
    
    return objets_selectionnes, valeur_totale, poids_total

# Liste d'objets
liste_objets=[(11, 9), (1, 1), (14, 1), (9, 1), (13, 13),(1, 12), (9, 14),(14, 10), (13, 6), (4, 5),(12, 1), (12, 2), (13, 12), (14, 15),(9, 3)]
# Masse maximale du sac à dos
masse_max = 30

# Utilisation de la fonction sac_a_dos avec le critère de tri sur la valeur
objets_selectionnes, valeur_totale, masse_totale = sac_a_dos(masse_max, liste_objets)

# Affichage des résultats
print("SELECTION SELON LA VALEUR")
print()
print("Objets sélectionnés :", objets_selectionnes)
print("Valeur totale :", valeur_totale)
print("Masse totale :", masse_totale)
print()

# # Question 2
def sac_a_dos2(masse_max, liste_objets):
    # trier les objets selon leur poids croissant
    sorted_objets = sorted(liste_objets, key=lambda x: x[1])
    masse_totale = 0
    valeur_totale = 0
    sac = []
    for objet in sorted_objets:
        if masse_totale + objet[1] <= masse_max:
            sac.append(objet)
            masse_totale += objet[1]
            valeur_totale += objet[0]
        else:
            break
    return sac, valeur_totale, masse_totale

# Liste d'objets
liste_objets=[(11, 9), (1, 1), (14, 1), (9, 1), (13, 13),(1, 12), (9, 14),(14, 10), (13, 6), (4, 5),(12, 1), (12, 2), (13, 12), (14, 15),(9, 3)]
# Masse maximale du sac à dos
masse_max = 30

# Utilisation de la fonction sac_a_dos2 avec le critère de tri sur le poids
objets_selectionnes, valeur_totale, masse_totale = sac_a_dos2(masse_max, liste_objets)

# Affichage des résultats
print("SELECTION SELON LE POIDS")
print()
print("Objets sélectionnés :", objets_selectionnes)
print("Valeur totale :", valeur_totale)
print("Masse totale :", masse_totale)
print()