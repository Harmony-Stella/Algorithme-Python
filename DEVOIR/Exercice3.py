pieces = [100, 50, 20, 10, 2, 1]

def rendre_monnaie(somme):
    nb_pieces = [0] * len(pieces)

    for i in range(len(pieces)):
        nb_pieces[i] = somme // pieces[i]
        somme = somme % pieces[i]

    return nb_pieces

# Demander à l'utilisateur de saisir un montant en euros
montant = int(input("Entrez le montant en euros à rendre : "))

# Utiliser l'algorithme glouton pour rendre la somme avec le minimum de pièces
nb_pieces = rendre_monnaie(montant)

# Afficher le nombre minimum de pièces de chaque valeur utilisé pour rendre la somme
print("Nombre de pièces utilisées pour rendre", montant, "cents d'euros :")
for i in range(len(nb_pieces)):
    if nb_pieces[i] > -1:
        print(nb_pieces[i], "pièce(s) de", pieces[i], "Euros")
