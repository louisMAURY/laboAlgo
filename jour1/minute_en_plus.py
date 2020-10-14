heure = input("Veuillez entrer un nombre de heures s'il vous plait 🙂 (entre 0 et 23)\n")
while int(heure) < 0 or int(heure) > 23:
    heure = input('Veuillez entrer un nombre correct !(entre 0 et 23)')

minutes = input("Veuillez entrer un nombre de minutes s'il vous plait 🙂 (entre 0 et 59)\n")
while int(minutes) < 0 or int(minutes) > 59:
    minutes = input("Veuillez entrer un nombre de minutes s'il vous plait 🙂 (entre 0 et 59)\n")

minutes = int(minutes) + 1
if minutes == 60:
    heure = int(heure) + 1
    minutes = 0

    if heure == 24:
        heure = 0

print('{}:{}'.format(heure, minutes))