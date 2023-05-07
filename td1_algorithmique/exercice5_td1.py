# Demande à l'utilisateur une valeur en secondes
duree_sec = int(input("Entrez une durée en secondes : "))

# Calcule le nombre d'heures, de minutes et de secondes correspondant
minutes, secondes = divmod(duree_sec, 60)
heures, minutes = divmod(minutes, 60)

# Affiche le résultat sous forme de texte
print("{:02d}:{:02d}:{:02d}".format(heures, minutes, secondes))
