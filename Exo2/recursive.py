def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)

# Demander à l'utilisateur d'entrer un nombre
n = int(input("Entrez un nombre : "))

# Calculer la factorielle de ce nombre
fact = factorielle(n)

# Afficher le résultat
print(f"La factorielle de {n} est {fact}.")