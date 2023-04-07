# Définition des objets
objets = [(2, 12), (1, 10), (4, 28), (3, 18), (6, 35)]

# Définition de la capacité maximale du sac à dos
capacite_max = 15

# Fonction pour calculer la valeur par unité de poids
def valeur_par_poids(objet):
    return objet[1] / objet[0]

# Tri des objets par ordre décroissant de leur valeur par unité de poids
objets_tries = sorted(objets, key=valeur_par_poids, reverse=True)

# Remplissage du sac à dos
poids_total = 0
valeur_totale = 0
for objet in objets_tries:
    if poids_total + objet[0] <= capacite_max:
        poids_total += objet[0]
        valeur_totale += objet[1]

# Affichage des résultats
print("Poids total dans le sac à dos :", poids_total)
print("Valeur totale des objets dans le sac à dos :", valeur_totale)
