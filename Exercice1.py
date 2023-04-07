def sontInvOuOpp(a, b):

    if a + b == 0:
            print("Les nombres {} et {} sont opposés".format(a, b))
            return True
    elif a * b == 1:
            print("Les nombres {} et {} sont inverses".format(a, b))
            return True
    else:
            print("Les nombres {} et {} ne sont ni opposés ni inverses".format(a, b))
            return False
        
continuer = True

while continuer:
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le deuxième nombre : "))
    sontInvOuOpp(a, b)

    choix = input("Voulez-vous continuer ? (oui/non) : ")
    if choix == "oui":
        continuer = True
    elif choix == "non":
        continuer = False
        print("----- Fin du programme,Merci!!! -----")
