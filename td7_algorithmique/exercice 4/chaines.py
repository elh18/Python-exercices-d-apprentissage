def compter(mot, lettre):
    compteur = 0
    for carac in mot:
        if carac == lettre:
            compteur += 1
    return compteur

def distincts(mot):
    liste_lettres = []
    for carac in mot:
        if not carac.isalpha():
            continue 
        # ignore les caractéres non alphabétiques, comme les espaces et la ponctuation
        elif carac.upper() not in liste_lettres:
            liste_lettres.append(carac.upper())
    return ''.join(liste_lettres)

def frequences(mot):
    dict_lettres = {}
    for carac in mot:
        if not carac.isalpha():
            # même chose ici, on ne compte que les lettres
            continue
        elif carac.upper() in dict_lettres:
            dict_lettres[carac.upper()] += 1
        else:
            dict_lettres[carac.upper()] = 1
    return dict_lettres

def inclusion(mot_1, mot_2):
    dict_lettres_1 = frequences(mot_1)
    dict_lettres_2 = frequences(mot_2)
    for lettre in dict_lettres_1:
        if lettre not in dict_lettres_2 or dict_lettres_1[lettre] > dict_lettres_2[lettre]:
            return False
    return True
