def afficher_resultats(voix_pour: int, voix_contre: int):
    """
    Fonction pour afficher les résultats des votes.
    :param voix_pour: le nombre de voix 'pour' le blocage de l'université
    :param voix_contre: le nombre de voix 'contre' le blocage de l'université
    """
    print("Nombre de voix pour le blocage :", voix_pour)
    print("Nombre de voix contre le blocage :", voix_contre)


def vote_blocage():
    """
    Fonction pour compter les voix lors d'une AG sur le blocage de l'université.
    """
    # Initialiser les compteurs
    voix_pour = 0
    voix_contre = 0

    # Lire chaque choix de l'étudiant
    for i in range(1, 601):
        choix = input(f"Étudiant {i}: Pour le blocage, répondez par 'OUI'. Contre le blocage, répondez par 'NON': ")

        # Vérifier le choix de l'étudiant
        if choix.upper() == "OUI":
            voix_pour += 1
        elif choix.upper() == "NON":
            voix_contre += 1

    # Afficher les résultats des votes
    afficher_resultats(voix_pour, voix_contre)

