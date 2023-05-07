# -*- coding: utf-8 -*-

#saisie du code de véhicule
code = input("code véhicule : ")

#conversion en numérique du code véhicule
code = float(code)

#saisie du kilométrage
k = input("Kilométrage : ")

#conversion en numérique du kilométrage
k = float(k)

#saisie nombre de jours
nj = input("Nombre de jours : ")

#conversion en numérique du nombre de jours
nj = float(nj)

#calcul du prix de la location si le nombre de jours est supérieur à 30 
if nj > 30 :
    ploc = 60 * nj

#calcul du prix de la location si le nombre de jours est inférieur à 30 et selon le code
elif code == 1 :
    ploc = 70 * nj + 0.5 * k

elif code == 2 :
    ploc = 60 * nj + 1.2 * k

#message d'erreur si le code n'est pas 1 ou 2
else :
    print("Erreur il y a que 2 code véhicule.")

#affichage du résultat
print("Prix de la location = ", ploc)