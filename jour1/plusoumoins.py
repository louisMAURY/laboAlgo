import random
# Choisir un nombre aléatoire
nb_choisi = random.randint(0, 100)
print(nb_choisi)

# Demander un nombre
nb_donne = input("Veuillez enter un nombre compris entre 0 et 100:\n")
while int(nb_donne) != nb_choisi:
    # si c'est plus grand que le nombre choisi
    if int(nb_donne) > nb_choisi:
        # Dire que c'est plus petit
        print("C'est plus petit 🔻")
    #Si c'est plus petit que le nombre choisi
    if int(nb_donne) < nb_choisi:
        # Dire que c'est plus grand
        print("C'est plus grand 🔺")

    nb_donne = input("Veuillez enter un nombre compris entre 0 et 100:\n")

# C'est gagné
print("C'est gagné !!")