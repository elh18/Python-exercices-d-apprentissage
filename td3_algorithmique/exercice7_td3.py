import random

# Initialisation des variables
nb_allumettes = random.randint(15, 20)
tour_joueur = True  # True pour le joueur, False pour l'ordinateur

# Fonction pour demander et vérifier la saisie du joueur
def demander_saisie():
    while True:
        saisie = input("Combien d'allumettes voulez-vous retirer (entre 1 et 3) ? ")
        if saisie.isdigit() and 1 <= int(saisie) <= 3 and int(saisie) <= nb_allumettes:
            return int(saisie)
        print("Saisie invalide. Veuillez entrer un nombre entre 1 et 3, et pas plus que le nombre d'allumettes restantes.")

# Déroulement du jeu
while nb_allumettes > 1:
    # Affichage du nombre d'allumettes restantes
    print("Il reste", nb_allumettes, "allumettes.")

    # Tour du joueur
    if tour_joueur:
        nb_retire = demander_saisie()
        nb_allumettes -= nb_retire
        print("Vous avez retiré", nb_retire, "allumettes.")
    # Tour de l'ordinateur
    else:
        # Stratégie de l'ordinateur : retirer le nombre nécessaire pour laisser un multiple de 4
        nb_retire = (nb_allumettes - 1) % 4
        if nb_retire == 0:
            nb_retire = random.randint(1, 3)
        nb_allumettes -= nb_retire
        print("L'ordinateur a retiré", nb_retire, "allumettes.")

    tour_joueur = not tour_joueur

# Affichage du résultat
if tour_joueur:
    print("Il ne reste plus qu'une allumette, vous avez gagné !")
else:
    print("Il ne reste plus qu'une allumette, l'ordinateur a gagné.")
