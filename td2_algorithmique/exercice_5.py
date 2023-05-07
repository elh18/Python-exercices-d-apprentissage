# -*- coding: utf-8 -*-

#saisie du salaire annuel de la mère
sm = input("Veuillez saisir le salaire annuel de la mère : ")

#conversion en numérique du  salaire annuel de la mère
sm = float(sm)

#saisie du salaire annuel du père
sp = input("Veuillez saisir le salaire annuel du père : ")

#conversion en numérique du salaire annuel du père
sp = float(sp)

#saisie du nombre d'enfant
ne = input("Veuillez saisir le nombre d'enfant au foyer : ")

#conversion en numérique du nombre d'enfant au foyer
ne = float(ne)

#calcul du quotient familiale
qf = (sm + sp)/(2+ne/2)

#calcul de l'imposition
if qf <= 5963 :
    print ("Le montant de votre imposition est 0.")

if 5963 < qf <= 11896 :
    impôt = (sm + sp)*0.055 - 327.97*(2+ne/2)

if 11896 < qf <= 26420 :
    impôt = (sm + sp)*0.14 - 1339.13*(2+ne/2)

if  26420< qf <= 70830 :
    impôt = (sm + sp)*0.3 - 5566.33*(2+ne/2)

if  70830 < qf :
    impôt = (sm + sp)*0.41 - 13357.63*(2+ne/2)

print  ("Voici le montant de votre imposition ", impôt)