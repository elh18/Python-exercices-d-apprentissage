import random

# Initialisation du générateur aléatoire
random.seed(None)

# Génération du nombre mystère
nombre_mystere = random.randint(1, 100)

# Initialisation du nombre d'essais
nb_essais = 0

# Boucle principale
while True:
    # Demande de saisie à l'utilisateur
    chiffre = int(input("Entrez un chiffre entre 1 et 100 : "))
    nb_essais += 1

    # Vérification de la saisie
    if chiffre < 1 or chiffre > 100:
        print("Le chiffre doit être compris entre 1 et 100")
        continue

    # Comparaison avec le nombre mystère
    if chiffre == nombre_mystere:
        print("Bravo, vous avez trouvé le nombre mystère en", nb_essais, "essais !")
        break
    elif chiffre < nombre_mystere:
        print("Votre", chiffre, "est plus petit que le nombre mystère.")
    else:
        print("Votre", chiffre, "est plus grand que le nombre mystère.")
