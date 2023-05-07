# Création d'un dictionnaire vide pour stocker les occurences des mots
dico_mots = {}

while True:
    # Demande à l'utilisateur d'entrer un mot en majuscule (la saisie se fait en minuscules et est transformée)
    mot = input("Veuillez entrer un mot ou tapez 'STOP' pour arrêter la saisie: ").upper()

    if mot == "STOP":
        break

    # Si le mot n'est pas dans le dictionnaire, on l'ajoute avec une valeur de 1
    if mot not in dico_mots:
        dico_mots[mot] = 1
    else:
        # Sinon, on incrémente la valeur correspondante
        dico_mots[mot] += 1

# On affiche les termes et leur nombre d'apparition en parcourant le dictionnaire
for k, v in dico_mots.items():
    print(f"{k} = {v}")
