def ajouter(L, x):
    liste = len(L)

    # on parcours la liste si elle est vide on retourne x
    if liste== 0:
        return [x]
    
    # si x est inferieur ou egal  à un élément de L on l'insert au tout début du tableau
    elif x <= L[0]:
        return [x] + L
    
    # si  x est superieur ou egal a un element de L on l'insert à la fin du tableau
    elif x >= L[liste-1]:
        return L + [x]
    
    #recherche dichotomique pour determiner la place x en utilisant l'indice 'gauche' ou 'droite'
    else:
        gauche = 0
        droite = liste-1
        while gauche < droite:
            milieu = (gauche + droite) // 2
            if x <= L[milieu]:
                droite = milieu
            else:
                gauche = milieu + 1
        return L[:gauche] + [x] + L[gauche:]
    
#Exemple de test du programme
L = [1, 3, 4]
x = 2
L = ajouter(L, x)
print(L) 
