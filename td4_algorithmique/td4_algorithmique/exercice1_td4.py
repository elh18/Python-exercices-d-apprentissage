# Demande à l'utilisateur la taille "n" de la liste
n = int(input("Entrez la taille de la liste : "))

# Crée une liste vide
liste = []

# Effectue la saisie des "n" valeurs et les insère dans la liste
for i in range(n):
    valeur = float(input("Entrez la valeur {}: ".format(i+1)))
    liste.append(valeur)

# Calcule et affiche la moyenne des valeurs de la liste
moyenne = sum(liste) / n
print("La moyenne est :", moyenne)

# Trie les valeurs de la liste de manière descendante selon la méthode des Tris à Bulles
tri_effectue = True
while tri_effectue:
    tri_effectue = False
    for i in range(n-1):
        if liste[i] < liste[i+1]:
            liste[i], liste[i+1] = liste[i+1], liste[i]
            tri_effectue = True

# Affiche la liste des valeurs triées
print("La liste triée est :", liste)

# Calcule et affiche la médiane de la liste de valeurs
if n % 2 == 0:
    mediane = (liste[n//2 - 1] + liste[n//2]) / 2
else:
    mediane = liste[n//2]
print("La médiane est :", mediane)
