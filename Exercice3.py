# Création du tableau contenant les lettres de l'alphabet
lettres_tab = []
for i in range(26):
    lettre = chr(ord('A') + i)
    lettres_tab.append(lettre)

# Première procédure : parcourir le tableau à 26 reprises
def frequence1(lettres_tab, chaine):
    # Initialisation du tableau de fréquences
    frequence = [0] * 26

    # Parcours du tableau et mise à jour des fréquences
    for i in range(len(chaine)):
        lettre_recuperer = chaine[i]
        index = ord(lettre_recuperer) - ord('A')
        frequence[index] += 1
    return frequence

# Deuxième procédure : parcourir le tableau une seule fois
def frequence2(lettres_tab, chaine):
    # Initialisation du tableau de fréquences
    frequence = [0] * 26

    # Parcours du tableau et mise à jour des fréquences
    for k in chaine:
        index = ord(k) - ord('A')
        frequence[index] += 1
    return frequence

# Fonction auxiliaire qui retourne la position d'une lettre dans l'alphabet
def position(lettre):
    return ord(lettre) - ord('A') + 1

# Boucle pour permettre à l'utilisateur d'entrer plusieurs lettres
while True:
    # Affichage du menu
    print("Que voulez-vous faire ?")
    print("1 - Trouver la fréquence d'une lettre majuscule")
    print("2 - Trouver la position d'une lettre majuscule dans l'alphabet")
    print("3 - Trouver la fréquence de chaque lettre dans une chaîne de caractères")
    print("4 - Afficher la position des lettres d'une chaîne de caractères dans l'alphabet")
    print("5 - Quitter le programme")
    choix = input("Entrez votre choix (1-5) : ")

    # Vérification de la validité du choix
    if choix not in ['1', '2', '3', '4', '5']:
        print("Choix invalide, veuillez réessayer.")
        continue

    # Demander à l'utilisateur d'entrer une lettre majuscule
    if choix == '1':
        lettre = input("Entrez une lettre majuscule : ")
        while len(lettre) != 1 or not lettre.isupper():
            lettre = input("Entrez une lettre majuscule : ")
        proc = input("Choisissez la procédure à utiliser (1 ou 2) : ")
        while proc not in ['1', '2']:
            proc = input("Choix invalide, veuillez réessayer (1 ou 2) : ")
        freq = frequence1(lettres_tab, lettre) if proc == '1' else frequence2(lettres_tab, lettre)
        pos = position(lettre)
        print(f"Fréquence de la lettre {lettre} : {freq[pos-1]}")

   # Afficher la position de chaque lettre de la chaîne par rapport à l'alphabet
    elif choix == '2':
        chaine = input("Entrez une chaîne de caractères : ")
        while not chaine.isalpha():
            chaine = input("Entrez une chaîne de caractères valide : ")
        positions = [position(lettre) for lettre in chaine]
        print("Position de chaque lettre dans l'alphabet : ")
        for i in range(len(chaine)):
            print(f"{chaine[i]} : {positions[i]}")

    # Demander à l'utilisateur d'entrer une chaîne de caractères et afficher la fréquence de chaque lettre
    elif choix == '3':
        chaine = input("Entrez une chaîne de caractères : ")
        while not chaine.isalpha():
            chaine = input("Entrez une chaîne de caractères valide : ")
        proc = input("Choisissez la procédure à utiliser (1 ou 2) : ")
        while proc not in ['1', '2']:
            proc = input("Choix invalide, veuillez réessayer (1 ou 2) : ")
        freq = frequence1(lettres_tab, chaine) if proc == '1' else frequence2(lettres_tab, chaine)
        print("Fréquence de chaque lettre : ")
        for i in range(len(lettres_tab)):
            print(f"{lettres_tab[i]} : {freq[i]}")

    
    # Demander à l'utilisateur d'entrer une chaîne de caractères
    elif choix == '4':
        chaine = input("Entrez une chaîne de caractères : ")
        for i in range(len(chaine)):
            lettre = chaine[i]
            pos = position(lettre)
            print(f"Position de la lettre {lettre} dans l'alphabet : {pos}")


        # Sortir de la boucle si l'utilisateur choisit de quitter le programme
    elif choix == '5':
        break


print("Au revoir !")
