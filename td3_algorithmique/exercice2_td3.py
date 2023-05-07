# Initialisation de la variable somme à 0
somme = 0

# Demande à l'utilisateur d'entrer une première valeur réelle positive (ou négative pour terminer)
valeur = float(input("Entrez une valeur réelle positive (ou une valeur négative pour terminer) : "))

# Boucle while pour ajouter les valeurs saisies à la somme tant que l'utilisateur entre des valeurs positives
while valeur >= 0:
    somme += valeur  # Ajoute la valeur saisie à la somme
    valeur = float(input("Entrez une valeur réelle positive (ou une valeur négative pour terminer) : "))  # Demande à l'utilisateur d'entrer une nouvelle valeur

# Vérifie si des saisies valides ont été effectuées et affiche le résultat
if somme == 0:
    print("Aucune saisie valide n'a été effectuée.")
else:
    print("La somme des valeurs saisies est : ", somme)
