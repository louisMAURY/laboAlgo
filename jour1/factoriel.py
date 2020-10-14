# Factoriel de 3 = 3*2*1

resultat = 1
nb_donne = int(input("Veuillez renter un nombre:\n"))

if nb_donne <= 1:
    resultat = 1
else:
    for i in range( 1, nb_donne + 1):
        resultat = resultat * i

print(resultat)