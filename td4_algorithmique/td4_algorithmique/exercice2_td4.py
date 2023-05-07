# Initialise une liste vide pour stocker les mots
liste_mots = []

# Saisie de la liste des mots
while True:
    mot = input("Entrez un mot (ou 'STOP' pour terminer) : ")
    if mot.upper() == "STOP":
        break
    liste_mots.append(mot.upper())

# Tri de la liste des mots par insertion
for i in range(1, len(liste_mots)):
    j = i - 1
    mot_a_inserer = liste_mots[i]
    while j >= 0 and mot_a_inserer < liste_mots[j]:
        liste_mots[j+1] = liste_mots[j]
        j -= 1
    liste_mots[j+1] = mot_a_inserer

# Affichage de la liste triée
print("La liste triée est :", liste_mots)

# Création d'un dictionnaire pour stocker les mots distincts et leur nombre d'apparition
dictionnaire_mots = {}
for mot in liste_mots:
    if mot not in dictionnaire_mots:
        dictionnaire_mots[mot] = liste_mots.count(mot)

# Affichage du dictionnaire des termes
print("Le dictionnaire des termes est :", list(dictionnaire_mots.keys()))

# Affichage du dictionnaire des termes et de leur nombre d'apparition
print("Le dictionnaire des termes et de leur nombre d'apparition est :")
for mot, count in dictionnaire_mots.items():
    print(mot, "=", count)
