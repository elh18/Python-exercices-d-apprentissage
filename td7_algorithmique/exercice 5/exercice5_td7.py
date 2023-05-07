from chaines import compter

mot = input("Entrez un mot : ")
lettre = input("Entrez une lettre : ")
mot = mot.upper()
lettre = lettre.upper()

nb_apparitions = compter(mot, lettre)

print(f"Le nombre d'apparitions de la lettre {lettre} dans le mot {mot} est {nb_apparitions}")
