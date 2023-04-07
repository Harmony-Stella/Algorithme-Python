def divise(p, q):
    # Vérifier si p divise q
    if q % p == 0:
        return True
    else:
        return False
    
# Demander à l'utilisateur d'entrer les valeurs de p et q
p = int(input("Entrez la valeur de p : "))
q = int(input("Entrez la valeur de q : "))

# Appel à la fonction divise(p, q)
if divise(p, q):
    print(f"True: {p} divise {q} ")
else:
    print(f"False: {p} ne divise pas {q}")
