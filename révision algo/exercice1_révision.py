# Initialisation des compteurs à 0
cpt1 = 0
cpt2 = 0

while True:
    # Lecture du salaire et conversion en float
    sal = float(input("Saisir le salaire : "))

    # Test de la valeur du salaire et incrémentation des compteurs
    if sal > 2000:
        cpt1 += 1
    elif sal < 1000:
        cpt2 += 1

    # Demande si l'utilisateur veut saisir un autre salaire
    rep = input("Voulez-vous saisir un autre salaire ? (O/N)")

    # Sortir de la boucle si l'utilisateur a répondu 'N'
    if rep == 'N':
        break

# Affichage des résultats
print("Le nombre de salaires > 2000 est :", cpt1)
print("Le nombre de salaires < 1000 est :", cpt2)

