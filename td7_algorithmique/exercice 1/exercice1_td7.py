import chaines  # Importation du module

# Saisie du mot et de la lettre
mot = input("Entrez un mot : ")
lettre = input("Entrez une lettre : ")

# Appel de la fonction compter du module chaines
nb_apparitions = chaines.compter(mot, lettre)

print(f"La lettre '{lettre}' apparait {nb_apparitions} fois dans le mot '{mot}'.")
