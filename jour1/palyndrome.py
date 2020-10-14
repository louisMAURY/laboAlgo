def palyndrome(mot):
    longueur = len(mot)
    compteur_bon = 0

    for i in range(longueur):
        print(mot[i], ':', mot[-i-1])
        if mot[i] == mot[-i-1]:
            compteur_bon += 1


    print(compteur_bon)
    if compteur_bon == longueur:
        return "C'est un palyndrome"
    else:
        return "Ce n'est pas un palyndrome"

print(palyndrome("pomme"))