# -*- coding: utf-8 -*-
#saisir prixHT
prixHT = float(input("saisir le prix HT :"))
#saisie Catégorie 
Cathégorie= input("préciser la cathgorie du produit si c’est de l’alimentaire par exemple  :  ")
alimentaire= str(input("alimentaire  :"))
#conversion en numerique  du prixTTC
prixTTC = float()
#calcul du prix TTC
if Cathégorie=="alimentaire" :
    prixTTC =prixHT*1.055
print ("le prix TTC est de", prixTTC ,"euros" )
if Cathégorie != "alimentaire" :
    prixTTC =prixHT*1.020
print ("le prix TTC est de", prixTTC ,"euros" )
