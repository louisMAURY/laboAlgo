import random

nb_choisi = random.randint(0, 100)


def plusoumoins():
    nb_donne = int(input('Entrez un nombre:\n'))

    if nb_donne > nb_choisi:
        print("C'est plus petit")
        plusoumoins()
    
    elif nb_donne < nb_choisi:
        print("C'est plus grand")
        plusoumoins()

    else:
        print("C'est gagné")


plusoumoins()