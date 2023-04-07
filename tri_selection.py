def tri_selection(tab):
    for i in range(len(tab)):
        min = i
        for j in range(i+1, len(tab)):
            if tab[min] > tab[j]:
                min = j
        tab[i], tab[min] = tab[min], tab[i]

# Exemple d'utilisation
liste = [64, 25, 12, 22, 11]
tri_selection(liste)
print("Liste triée:")
for i in range(len(liste)):
    print("%d" %liste[i])