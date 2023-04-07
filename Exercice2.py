def existeInvOuOppConsecutifs(T):
    n = len(T)
    found = False
    for i in range(n-1):
        a = T[i]
        b = T[i+1]
        if a + b == 0:
            print("Les nombres {} et {} sont opposés et consécutifs dans le tableau".format(a, b))
            found = True
        elif a * b == 1:
            print("Les nombres {} et {} sont inverses et consécutifs dans le tableau".format(a, b))
            found = True
    if found:
        return True
    else:
        return False

T = []
taille = int(input("Entrez la taille du tableau : "))
for i in range(taille):
    nombre = float(input("Entrez un nombre pour le tableau : "))
    T.append(nombre)

resultat = existeInvOuOppConsecutifs(T)
print(resultat)
if resultat:
    print("Le tableau contient au moins deux nombres consécutifs opposés ou inverses.")
else:
    print("Le tableau ne contient pas deux nombres consécutifs opposés ou inverses.")
