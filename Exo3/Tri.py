def tri_selection(t):
    n = len(t)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if t[j] < t[min_index]:
                min_index = j
        t[i], t[min_index] = t[min_index], t[i]  # Échanger l'élément courant avec le plus petit élément trouvé

# Test de la procédure tri_selection
t1 = [5, 3, 8, 6, 2, 7, 1, 4]
tri_selection(t1)
print(t1)  # Devrait afficher [1, 2, 3, 4, 5, 6, 7, 8]

t2 = [1, 2, 3, 4, 5]
tri_selection(t2)
print(t2)  # Devrait afficher [1, 2, 3, 4, 5]

t3 = [5, 4, 3, 2, 1]
tri_selection(t3)
print(t3)  # Devrait afficher [1, 2, 3, 4, 5]


# Nombre maximal d'échanges
# Dans le pire des cas, chaque élément du tableau sera échangé n-1 fois
# donc le nombre maximal d'échanges est n*(n-1)/2
n = 5
max_echanges = n*(n-1)/2
print(f"Le nombre maximal d'échanges est de {max_echanges}")