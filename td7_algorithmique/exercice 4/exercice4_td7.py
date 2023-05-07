import chaines

mot_1 = input("Saisir le premier mot : ")
mot_2 = input("Saisir le deuxième mot : ")

mot_1 = mot_1.upper()
mot_2 = mot_2.upper()

if chaines.inclusion(mot_1, mot_2):
    print(f"{mot_1} est inclus dans {mot_2}")
else:
    print(f"{mot_1} n'est pas inclus dans {mot_2}")
