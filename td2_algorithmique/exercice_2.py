# -*- coding: utf-8 -*-

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

#calcul du prix de la location si le nombre de jours est inférieur à 30
if nj < 30 :
    ploc = 50 * nj + 0.7 * k

#affichage du résultat
print("Prix de la location = ", ploc)