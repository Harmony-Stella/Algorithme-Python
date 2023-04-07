import random

# Saisie du nombre d'éléments
n = int(input("Entrez le nombre d'éléments : "))

# Initialisation du tableau avec des valeurs aléatoires
tableau = [random.randint(0, 20) for i in range(n)]

# Affichage du tableau avant le tri
print("Tableau avant le tri : ", tableau)

# Algorithme de tri par sélection
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if tableau[min_idx] > tableau[j]:
            min_idx = j
    tableau[i], tableau[min_idx] = tableau[min_idx], tableau[i]

# Affichage du tableau après le tri
print("Tableau après le tri : ", tableau)
