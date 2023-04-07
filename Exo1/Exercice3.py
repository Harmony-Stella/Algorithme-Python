def estpremier(p):
    if p <= 1:  # Les nombres inférieurs ou égaux à 1 ne sont pas premiers
        return False
    elif p == 2:  # 2 est un nombre premier
        return 1
    else:
        for i in range(2, int(p**0.5) + 1):  # On teste tous les diviseurs potentiels de p jusqu'à sa racine carrée
            if p % i == 0:  # Si p est divisible par un nombre autre que 1 et lui-même, alors p n'est pas premier
                return 0
        return 1  # Si p n'est divisible par aucun nombre autre que 1 et lui-même, alors p est premier

def phi(n):
    count = 0
    for i in range(2, n+1):
        if estpremier(i):
            count += 1
    return count

# Demander à l'utilisateur d'entrer le nombre à vérifier
p = int(input("Entrez un nombre : "))

# Vérifier si le nombre est premier ou non
if estpremier(p):
    print(f"{p} est un nombre premier.")
else:
    print(f"{p} n'est pas un nombre premier.")
    
# Calculer le nombre de nombres premiers inférieurs ou égaux au nombre donné
n = phi(p)
print(f"Il y a {n} nombres premiers inférieurs ou égaux à {p}.")